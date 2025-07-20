from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()


class REDIS_SECRETS(str, Enum):
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
    REDIS_USERNAME = os.environ.get("REDIS_USERNAME")


class JWT_SECRETS:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


class API_KEYS:
    GOOGLE_GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


class LLM_MODELS:
    GOOGLE_GEMINI_MODEL = "gemini-2.5-flash"


class GMAIL_CREDS:
    APP_PASSWORD = os.environ.get("XPLORE_GMAIL_APP_PASSWORD")


class OTP_TYPE(Enum):
    SIGN_UP = "sign-up"
    SIGN_IN = "sign-in"
    RESET_PASSWORD = "reset-password"
