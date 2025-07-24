import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv('TOKEN')
DB_LITE = os.getenv('DB_LITE')
