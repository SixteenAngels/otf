from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os
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

# Define allowed origins
origins = [
    "https://concert-frontend.onrender.com",
    "http://localhost:3000",
]


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
    try:
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


# Mount frontend static files if they exist
frontend_build_path = Path(__file__).parent.parent / "frontend" / "build"
if frontend_build_path.exists():
    print(f"Mounting frontend build from {frontend_build_path}")
    app.mount("/assets", StaticFiles(directory=frontend_build_path / "static"), name="static")
    
    # Serve index.html for all non-API routes (SPA routing)
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        """Serve the React app for SPA routing."""
        # Don't intercept API routes
        if full_path.startswith("api/"):
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Not found")
        
        # Serve index.html for all other routes
        index_path = frontend_build_path / "index.html"
        if index_path.exists():
            with open(index_path, 'r') as f:
                from fastapi.responses import HTMLResponse
                return HTMLResponse(content=f.read())
        
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Frontend not available")
else:
    print(f"Frontend build not found at {frontend_build_path}")

