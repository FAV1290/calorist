from telegram.ext import ContextTypes
from telegram import ForceReply, Update, Message, User


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Message:
    user: User | None = update.effective_user
    if user:
        return update.message.reply_html(rf'Hi {user.mention_html()}!', reply_markup=ForceReply(selective=True))
