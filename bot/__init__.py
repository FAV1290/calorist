from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler


from bot.logger import init_logger
from bot.config import BOT_TOKEN
from bot.handlers import start_handler


logger = init_logger()


class CaloristTGBot():
    def __init__(self, bot_token: str = BOT_TOKEN):
        self.bot = ApplicationBuilder().token(bot_token).build()
        self.bot.add_handler(CommandHandler('start', start_handler))
    
    def run(self) -> None:
        self.bot.run_polling(allowed_updates=Update.ALL_TYPES)
