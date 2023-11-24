import logging


from bot.config import LOGGING_FORMAT


def init_logger() -> logging.Logger:
    logging.basicConfig(filename='calorist.log', format=LOGGING_FORMAT, level=logging.INFO)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    return logging.getLogger(__name__)
