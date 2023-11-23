from telegram.ext import ContextTypes
from telegram import Update


from db.models import Ingredient
from bot.context_managers import add_user_id_to_context


async def ingredients_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message
    user_id = add_user_id_to_context(update, context)
    ingredients = Ingredient.fetch_user_ingredients(user_id)
    ingredients_report = 'Your ingredients:' if ingredients else 'No ingredients found'
    for item in ingredients:
        ingredient_str = f'\n• {item.name.capitalize()} '
        ingredient_str += f'({item.kcals}/{item.proteins}/{item.fats}/{item.carbohydrates})'
        ingredients_report += ingredient_str
    await update.message.reply_text(ingredients_report)
