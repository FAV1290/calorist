from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters


from db.models import Ingredient
from db.changers import add_object
from bot.enums import IngredientAddStage
from apps.converters import compose_ingredient_from
from bot.context_managers import add_user_id_to_context
from apps.validators import validate_ingredient_name, validate_nutrition_facts


async def start_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    assert update.message
    await update.message.reply_text('Please type ingredient name or /cancel to leave')
    return IngredientAddStage.NAME


async def check_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    assert update.message and context.user_data is not None
    raw_ingredient_name = update.message.text or ''
    user_id = add_user_id_to_context(update, context)
    user_ingredients_names = list(map(lambda x: x.name, Ingredient.fetch_user_ingredients(user_id)))
    is_name_valid, feedback = validate_ingredient_name(raw_ingredient_name, user_ingredients_names)
    if is_name_valid:
        context.user_data['ingredient_name'] = raw_ingredient_name.strip().lower()
        nutrition_facts_message = '\n'.join([
            'Got it! Now type ingredient nutrition facts',
            '(kcals, proteins, fats, carbohydrates), separated by space',
            'or /cancel to leave. For example: 50.00 2.00 0.00 11.00',
        ])
        await update.message.reply_text(nutrition_facts_message)
        return IngredientAddStage.NUTRITION_FACTS
    else:
        await update.message.reply_text(f'{feedback}. Please try again or type /cancel to leave')
        return IngredientAddStage.NAME


async def check_nutrition_facts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    assert update.message and context.user_data is not None
    nutrition_facts = (update.message.text or '').replace(',', '.').split(' ')
    are_nutrition_facts_valid, feedback = validate_nutrition_facts(nutrition_facts)
    if are_nutrition_facts_valid:
        new_ingredient = compose_ingredient_from(
            context.user_data['ingredient_name'],
            context.user_data['user_id'],
            *list(map(lambda x: float(x), nutrition_facts)),
        )
        add_object(new_ingredient)
        await update.message.reply_text('New ingredient successfully added')
        return ConversationHandler.END
    else:
        await update.message.reply_text(f'{feedback}. Please try again or type /cancel to leave')
        return IngredientAddStage.NUTRITION_FACTS


async def cancel_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message:
        await update.message.reply_text('Ingredient add canceled')
    return ConversationHandler.END


def init_ingredient_add_handler() -> ConversationHandler:
    return ConversationHandler(
        entry_points=[CommandHandler('add_ingredient', start_conversation)],
        states={
            IngredientAddStage.NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_name)],
            IngredientAddStage.NUTRITION_FACTS: [MessageHandler(
                filters.TEXT & ~filters.COMMAND, check_nutrition_facts)],
        },
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
