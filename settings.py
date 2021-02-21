from dotenv import load_dotenv
import os

load_dotenv('.env')
Y2B_URL = os.getenv('Y2B_URL')
Y2B_KEY = os.getenv('Y2B_KEY')

TRANS_URL = os.getenv('TRANS_URL')
TRANS_KEY = os.getenv('TRANS_KEY')

UNSPLASH_URL = os.getenv('UNSPLASH_URL')
UNSPLASH_KEY = os.getenv('UNSPLASH_KEY')
