import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_TOKEN_EXPIRED = int(os.getenv("JWT_TOKEN_EXPIRED", "3600"))
