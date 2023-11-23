from telegram.ext import ContextTypes
from telegram import ForceReply, Update


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.effective_user and update.message
    user = update.effective_user
    start_message = rf'Hi {user.mention_html()}. Your telegram id is {user.id}!'
    await update.message.reply_html(start_message, reply_markup=ForceReply(selective=True))
