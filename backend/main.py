from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    auth_router,
    concert_router,
    ticket_router,
    scan_router,
    transfer_router
)

app = FastAPI(
    title="Concert Ticket QR System",
    description="API for managing concert tickets with QR codes, authentication, and attendance tracking",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth_router)
app.include_router(concert_router)
app.include_router(ticket_router)
app.include_router(scan_router)
app.include_router(transfer_router)


# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup if needed."""
    import asyncio
    import os
    try:
        if os.getenv("DATABASE_URL"):
            from init_db import init_db, seed_users, seed_concert
            print("Initializing database on startup...")
            await init_db()
            await seed_users()
            await seed_concert()
            print("Database initialized successfully!")
    except Exception as e:
        print(f"Database initialization warning: {e}")
        # Don't crash the server if initialization fails


@app.get("/")
def read_root():
    """Root endpoint."""
    print("DEBUG: Root endpoint called")
    return {
        "message": "Concert Ticket QR System API v2.0",
        "docs": "/docs",
        "health": "ok",
        "features": [
            "User authentication",
            "Concert management",
            "Ticket QR generation",
            "Sales & attendance tracking",
            "Ticket transfers"
        ]
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    print("DEBUG: Health endpoint called")
    return {"status": "healthy"}

