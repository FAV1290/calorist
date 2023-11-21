import logging
from telegram import ForceReply, Update
from telegram.ext import ContextTypes


from bot.config import LOGGING_FORMAT


logging.basicConfig(filename='calorist.log', format=LOGGING_FORMAT, level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    return update.message.reply_html(rf"Hi {user.mention_html()}!", reply_markup=ForceReply(selective=True))


def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    return update.message.reply_text("Help!")


def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    return update.message.reply_text(update.message.text)
