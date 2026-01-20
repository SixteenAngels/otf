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
    from app.models.user import UserRole
    
    users = [
        # Admin
        User(username="otf", email="admin@otf.com", hashed_password=get_password_hash("cows12"), role=UserRole.ADMIN),
        
        # Sales users (Stage 1) - use SCANNER role
        User(username="sales1", email="sales1@concert.com", hashed_password=get_password_hash("vmpxJs"), role=UserRole.SCANNER),
        User(username="sales2", email="sales2@concert.com", hashed_password=get_password_hash("0v5m7B"), role=UserRole.SCANNER),
        User(username="sales3", email="sales3@concert.com", hashed_password=get_password_hash("PXRPvS"), role=UserRole.SCANNER),
        User(username="sales4", email="sales4@concert.com", hashed_password=get_password_hash("zXfaX8"), role=UserRole.SCANNER),
        User(username="sales5", email="sales5@concert.com", hashed_password=get_password_hash("no9LzA"), role=UserRole.SCANNER),
        User(username="sales6", email="sales6@concert.com", hashed_password=get_password_hash("fkRaMf"), role=UserRole.SCANNER),
        User(username="sales7", email="sales7@concert.com", hashed_password=get_password_hash("GlXaHW"), role=UserRole.SCANNER),
        User(username="sales8", email="sales8@concert.com", hashed_password=get_password_hash("MZvd6C"), role=UserRole.SCANNER),
        User(username="sales9", email="sales9@concert.com", hashed_password=get_password_hash("P5Q0PM"), role=UserRole.SCANNER),
        User(username="sales10", email="sales10@concert.com", hashed_password=get_password_hash("PxPove"), role=UserRole.SCANNER),
        
        # Verify users (Stage 2) - use VIEWER role
        User(username="verify1", email="verify1@concert.com", hashed_password=get_password_hash("kWYzRa"), role=UserRole.VIEWER),
        User(username="verify2", email="verify2@concert.com", hashed_password=get_password_hash("a7WMYT"), role=UserRole.VIEWER),
        User(username="verify3", email="verify3@concert.com", hashed_password=get_password_hash("IQnj28"), role=UserRole.VIEWER),
        User(username="verify4", email="verify4@concert.com", hashed_password=get_password_hash("6nGzr9"), role=UserRole.VIEWER),
        User(username="verify5", email="verify5@concert.com", hashed_password=get_password_hash("yBWP8l"), role=UserRole.VIEWER),
        User(username="verify6", email="verify6@concert.com", hashed_password=get_password_hash("L9TDtv"), role=UserRole.VIEWER),
        User(username="verify7", email="verify7@concert.com", hashed_password=get_password_hash("SXQzc9"), role=UserRole.VIEWER),
        User(username="verify8", email="verify8@concert.com", hashed_password=get_password_hash("S8dvXP"), role=UserRole.VIEWER),
        User(username="verify9", email="verify9@concert.com", hashed_password=get_password_hash("vlMEmz"), role=UserRole.VIEWER),
        User(username="verify10", email="verify10@concert.com", hashed_password=get_password_hash("BFnVZt"), role=UserRole.VIEWER),
    ]
    
    async with async_session() as session:
        for user in users:
            session.add(user)
        await session.commit()
    
    print(f"✓ Seeded {len(users)} users (1 admin, 10 scanners, 10 viewers)")

async def seed_concert():
    """Seed test concert"""
    from app.database import async_session
    from datetime import datetime
    
    concert = Concert(
        name="Test Concert",
        venue="Test Venue",
        date=datetime(2025, 6, 15),
        description="A test concert for the QR system"
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
