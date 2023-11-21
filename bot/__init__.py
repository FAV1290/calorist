import logging
from telegram import Update
from telegram.ext import Application, CommandHandler,  MessageHandler, filters


from bot.config import LOGGING_FORMAT, BOT_TOKEN
from bot.handlers import start_handler, help_handler, echo_handler


logging.basicConfig(filename='calorist.log', format=LOGGING_FORMAT, level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class CaloristTGBot():
    def __init__(self, bot_token: str = BOT_TOKEN):
        self.bot = Application.builder().token(bot_token).build()
        self.bot.add_handler(CommandHandler("start", start_handler))
        self.bot.add_handler(CommandHandler("help", help_handler))
        self.bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    
    def run(self) -> None:
        self.bot.run_polling(allowed_updates=Update.ALL_TYPES)
