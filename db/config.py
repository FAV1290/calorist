import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


DB_HOST = os.environ['CALORIST_DB_HOST']
