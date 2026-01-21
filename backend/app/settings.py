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

# Use DATABASE_URL from environment if available and not localhost
if os.getenv("DATABASE_URL") and "localhost" not in os.getenv("DATABASE_URL"):
    settings.database_url = os.getenv("DATABASE_URL")

# If we have a postgresql URL, make sure it's async
if settings.database_url and settings.database_url.startswith("postgresql://"):
    settings.database_url = settings.database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

# If no database_url is set by now, default to sqlite
if not settings.database_url:
    settings.database_url = "sqlite+aiosqlite:///./concert_tickets.db"
