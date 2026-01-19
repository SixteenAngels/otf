from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Default to SQLite, but allow PostgreSQL in production
    database_url: Optional[str] = None
    env: str = "development"
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()

# Determine database URL based on environment
if settings.env == "production" and settings.database_url and "postgresql" in settings.database_url:
    # Production with PostgreSQL
    pass
elif os.getenv("DATABASE_URL") and "localhost" not in os.getenv("DATABASE_URL"):
    # Valid external database URL
    settings.database_url = os.getenv("DATABASE_URL")
elif os.getenv("DATABASE_URL") is None or "localhost" in os.getenv("DATABASE_URL"):
    # No valid DB URL, use SQLite
    settings.database_url = "sqlite+aiosqlite:///./concert_tickets.db"
    
# Final fallback
if not settings.database_url:
    settings.database_url = "sqlite+aiosqlite:///./concert_tickets.db"
