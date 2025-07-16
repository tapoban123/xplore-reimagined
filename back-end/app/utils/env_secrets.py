from enum import Enum
from dotenv import load_dotenv
import os

load_dotenv()


class JWT_SECRETS(Enum):
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


class API_KEYS(Enum):
    GOOGLE_GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


class LLM_MODELS():
    GOOGLE_GEMINI_MODEL = "gemini-2.5-flash"
