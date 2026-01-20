"""Initialize database and seed accounts"""
import asyncio
import os
import sys
from app.database import engine
from app.models.base import Base
from app.models.user import User
from app.models.concert import Concert
from app.utils.auth import get_password_hash

# Debug: Print database URL being used
db_url = os.getenv("DATABASE_URL", "sqlite:///./concert_tickets.db")
print(f"Using database: {db_url[:50]}...")

async def init_db():
    """Create all tables"""
    try:
        async with engine.begin() as conn:
            print("Dropping tables...")
            await conn.run_sync(Base.metadata.drop_all)
            print("Creating tables...")
            await conn.run_sync(Base.metadata.create_all)
            print("✓ Tables created")
    except Exception as e:
        print(f"ERROR during init_db: {e}")
        import traceback
        traceback.print_exc()
        raise

async def seed_users():
    """Seed test users"""
    from app.database import async_session
    
    users = [
        # Admin
        User(username="otf", email="admin@otf.com", password_hash=get_password_hash("cows12"), role="admin"),
        
        # Sales users (Stage 1)
        User(username="sales1", email="sales1@concert.com", password_hash=get_password_hash("vmpxJs"), role="sales"),
        User(username="sales2", email="sales2@concert.com", password_hash=get_password_hash("0v5m7B"), role="sales"),
        User(username="sales3", email="sales3@concert.com", password_hash=get_password_hash("PXRPvS"), role="sales"),
        User(username="sales4", email="sales4@concert.com", password_hash=get_password_hash("zXfaX8"), role="sales"),
        User(username="sales5", email="sales5@concert.com", password_hash=get_password_hash("no9LzA"), role="sales"),
        User(username="sales6", email="sales6@concert.com", password_hash=get_password_hash("fkRaMf"), role="sales"),
        User(username="sales7", email="sales7@concert.com", password_hash=get_password_hash("GlXaHW"), role="sales"),
        User(username="sales8", email="sales8@concert.com", password_hash=get_password_hash("MZvd6C"), role="sales"),
        User(username="sales9", email="sales9@concert.com", password_hash=get_password_hash("P5Q0PM"), role="sales"),
        User(username="sales10", email="sales10@concert.com", password_hash=get_password_hash("PxPove"), role="sales"),
        
        # Verify users (Stage 2)
        User(username="verify1", email="verify1@concert.com", password_hash=get_password_hash("kWYzRa"), role="verify"),
        User(username="verify2", email="verify2@concert.com", password_hash=get_password_hash("a7WMYT"), role="verify"),
        User(username="verify3", email="verify3@concert.com", password_hash=get_password_hash("IQnj28"), role="verify"),
        User(username="verify4", email="verify4@concert.com", password_hash=get_password_hash("6nGzr9"), role="verify"),
        User(username="verify5", email="verify5@concert.com", password_hash=get_password_hash("yBWP8l"), role="verify"),
        User(username="verify6", email="verify6@concert.com", password_hash=get_password_hash("L9TDtv"), role="verify"),
        User(username="verify7", email="verify7@concert.com", password_hash=get_password_hash("SXQzc9"), role="verify"),
        User(username="verify8", email="verify8@concert.com", password_hash=get_password_hash("S8dvXP"), role="verify"),
        User(username="verify9", email="verify9@concert.com", password_hash=get_password_hash("vlMEmz"), role="verify"),
        User(username="verify10", email="verify10@concert.com", password_hash=get_password_hash("BFnVZt"), role="verify"),
    ]
    
    async with async_session() as session:
        for user in users:
            session.add(user)
        await session.commit()
    
    print(f"✓ Seeded {len(users)} users (1 admin, 10 sales, 10 verify)")

async def seed_concert():
    """Seed test concert"""
    from app.database import async_session
    
    concert = Concert(
        name="Test Concert",
        venue="Test Venue",
        date="2025-06-15",
        total_tickets=100
    )
    
    async with async_session() as session:
        session.add(concert)
        await session.commit()
    
    print("✓ Seeded test concert")

async def main():
    print("Initializing database...")
    await init_db()
    await seed_users()
    await seed_concert()
    print("✓ Database initialization complete!")

if __name__ == "__main__":
    asyncio.run(main())
