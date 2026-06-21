import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration management."""
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    DEFAULT_MODEL = "gemini-2.5-flash"
    DEFAULT_EMBEDDING_MODEL = "models/text-embedding-004"
