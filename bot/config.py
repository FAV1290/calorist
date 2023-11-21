import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

BOT_TOKEN = os.environ['CALORIST_BOT_TOKEN']
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
