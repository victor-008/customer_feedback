from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_URL = os.getenv("DB_URL")
#DB_URL = "sqlite:///./feedback.db" #incase of failure of os.getenv
LOG_LEVEL = os.getenv("LOG_LEVEL")
MODEL_NAME = os.getenv("MODEL_NAME")