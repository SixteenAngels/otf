"""Initialize database and seed accounts"""
import asyncio
from app.database import engine
from app.models.base import Base
from app.models.user import User
from app.models.concert import Concert
from app.utils.auth import get_password_hash

async def init_db():
    """Create all tables"""
    async with engine.begin() as conn:
        print("Dropping tables...")
        await conn.run_sync(Base.metadata.drop_all)
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("✓ Tables created")

async def seed_users():
    """Seed test users"""
    from app.database import async_session
    
    users = [
        User(username="otf", email="otf@test.com", password_hash=get_password_hash("cows12"), role="admin"),
        User(username="sales1", email="sales1@test.com", password_hash=get_password_hash("sales1"), role="sales"),
        User(username="verify1", email="verify1@test.com", password_hash=get_password_hash("verify1"), role="verify"),
    ]
    
    async with async_session() as session:
        for user in users:
            session.add(user)
        await session.commit()
    
    print(f"✓ Seeded {len(users)} users")

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
