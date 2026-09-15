import os
from pathlib import Path
from dotenv import load_dotenv
import pymysql as mysql


load_dotenv(Path(__file__).resolve().parents[1] / ".env")


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "cursorclass": mysql.cursors.DictCursor,
    "connect_timeout": 5,
}

def get_connection():
    return mysql.connect(**DB_CONFIG)
