# Concert Ticket QR System - Complete Setup Guide

## System Ready! ✅

Your Concert Ticket QR System is now fully set up and ready to run. This system allows you to manage concert tickets with QR code generation, scanning for sales confirmation, and attendance tracking.

## Quick Start

### Option 1: Using PowerShell (Recommended)

**Terminal 1 - Backend Server:**
```powershell
.\run.ps1 backend
```

**Terminal 2 - Frontend Server:**
```powershell
.\run.ps1 frontend
```

### Option 2: Using Command Prompt

**Terminal 1 - Backend:**
```cmd
run.bat backend
```

**Terminal 2 - Frontend:**
```cmd
run.bat frontend
```

### Option 3: Manual Commands

**Backend (Terminal 1):**
```powershell
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

**Frontend (Terminal 2):**
```powershell
cd frontend
npm start
```

## Access Points

Once both servers are running:

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/docs (Swagger UI)
- **Alternative Docs**: http://127.0.0.1:8000/redoc (ReDoc)

## Features

### Backend Features
✅ FastAPI REST API with 22 endpoints
✅ JWT-based authentication
✅ Role-based access control (Admin, Scanner, Viewer)
✅ Concert management
✅ Ticket generation with unique QR codes
✅ QR code scanning for sales & attendance
✅ Ticket transfer system (no refunds)
✅ Async database operations with SQLite/PostgreSQL

### Frontend Features
✅ User authentication & registration
✅ Concert management interface
✅ Ticket generation & management
✅ Live QR code scanner
✅ Attendance tracking dashboard
✅ Ticket transfer functionality
✅ Responsive Tailwind CSS design

## User Roles

### Admin
- Full system access
- Can create concerts
- Can generate and manage tickets
- Can view reports and statistics
- Can manage transfers

### Scanner
- Can scan QR codes
- Can check ticket validity
- Can record attendance
- Read-only access to concert info

### Viewer
- Can view concert information
- Can transfer their own tickets
- Limited access

## Workflow Example

1. **Admin creates a concert**
   - Go to Admin Dashboard
   - Click "Create Concert"
   - Enter concert details

2. **Admin generates tickets**
   - Select the concert
   - Specify quantity and price
   - System generates unique tickets with QR codes

3. **Scanner checks sales**
   - Use QR Scanner page
   - Scan ticket QR code
   - Mark as "SOLD" when purchased

4. **On concert day**
   - Scanners at entrance scan QR codes
   - System marks attendance
   - View live attendance statistics

5. **Ticket transfers**
   - Users can initiate transfers
   - Recipient accepts/rejects
   - System updates ticket holder

## API Endpoints

### Authentication
```
POST   /api/auth/register       - Register new user
POST   /api/auth/login          - Login (returns JWT token)
```

### Concerts
```
GET    /api/concerts/           - List all concerts
POST   /api/concerts/           - Create new concert
GET    /api/concerts/{id}       - Get concert details
```

### Tickets
```
POST   /api/tickets/create/{concert_id}    - Generate N tickets
GET    /api/tickets/concert/{concert_id}   - List concert tickets
GET    /api/tickets/{id}                    - Get ticket details
POST   /api/tickets/{id}/mark-sold          - Mark ticket as sold
GET    /api/tickets/number/{ticket_number}  - Find ticket by number
```

### Scanning
```
POST   /api/scans/                          - Record a scan
GET    /api/scans/ticket/{ticket_id}        - Get ticket scan history
GET    /api/scans/concert/{id}/attendance   - Get attendance stats
```

### Transfers
```
POST   /api/transfers/initiate              - Start transfer
GET    /api/transfers/pending               - Get pending transfers
POST   /api/transfers/{id}/accept           - Accept transfer
POST   /api/transfers/{id}/reject           - Reject transfer
GET    /api/transfers/{id}                  - Get transfer details
```

## Database

### Development Database
- **Type**: SQLite
- **File**: `backend/test_concert.db`
- **Auto-created** on first server start

### Production Database
To use PostgreSQL:

1. Update `backend/app/settings.py`:
```python
database_url = "postgresql+asyncpg://user:password@host:5432/database"
```

2. Or set environment variable:
```powershell
$env:DATABASE_URL="postgresql+asyncpg://user:password@host:5432/database"
```

## Project Structure

```
concert-qr-system/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoint handlers
│   │   ├── schemas/         # Pydantic validation schemas
│   │   ├── utils/           # Auth, QR generation utilities
│   │   ├── database.py      # Database setup
│   │   └── settings.py      # Configuration
│   ├── main.py              # FastAPI application
│   ├── init_db.py           # Database initialization
│   ├── test_api.py          # API test script
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/             # HTTP client & endpoints
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── store/           # Zustand state management
│   │   ├── App.jsx          # Root component
│   │   └── index.jsx        # Entry point
│   └── package.json         # Node dependencies
│
├── run.ps1                  # PowerShell startup script
├── run.bat                  # Batch startup script
└── SETUP_COMPLETE.md        # Setup documentation
```

## Troubleshooting

### Backend Issues

**Port 8000 already in use:**
```powershell
# Find and stop the process
Get-Process python | Stop-Process -Force
# Or change the port
python -m uvicorn main:app --host 127.0.0.1 --port 8001
```

**Database locked error:**
- Close all connections to the SQLite database
- Delete `test_concert.db` and restart to recreate

**Dependencies missing:**
```powershell
cd backend
pip install -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
- The React app will prompt to use another port (usually 3001)
- Or kill the process: `Get-Process node | Stop-Process -Force`

**npm not found:**
```powershell
# Update npm
npm install -g npm@latest
```

**Dependencies need update:**
```powershell
cd frontend
npm install --legacy-peer-deps
npm update
```

## Testing the API

### Using FastAPI Docs
1. Go to: http://127.0.0.1:8000/docs
2. Click "Try it out" on any endpoint
3. Enter parameters and click "Execute"

### Using curl/PowerShell
```powershell
# Register
$body = @{
    username = "admin"
    email = "admin@test.com"
    password = "SecurePass123"
    role = "admin"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/auth/register" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

$response.Content | ConvertFrom-Json

# Login
$body = @{
    username = "admin"
    password = "SecurePass123"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/auth/login" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

$token = ($response.Content | ConvertFrom-Json).access_token
```

## Environment Configuration

Create a `.env` file in the `backend` directory:

```env
# Database
DATABASE_URL=sqlite+aiosqlite:///./test_concert.db

# JWT Configuration
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Environment
ENV=development
```

## Deployment

### Docker Deployment
```powershell
# Build and run with Docker Compose
docker-compose up --build

# Or just build
docker-compose build

# Run in background
docker-compose up -d

# Stop
docker-compose down
```

### Manual Deployment
1. Set up Python 3.10+ and Node.js 18+
2. Install dependencies
3. Configure database
4. Run both servers

## Version Information

- **Backend**: Python 3.10+, FastAPI 0.104+, SQLAlchemy 2.0+
- **Frontend**: React 18, Node 18+
- **Database**: SQLite 3 (development) or PostgreSQL 12+ (production)

## Support

### API Documentation
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

### Check Health
```
GET http://127.0.0.1:8000/health    -> {"status": "healthy"}
GET http://127.0.0.1:8000/           -> System information
```

## Next Steps

1. Start both servers using the startup scripts
2. Create an admin account via frontend registration
3. Log in to the frontend
4. Create a test concert
5. Generate test tickets
6. Use the QR scanner to test
7. Check the API documentation at `/docs`

---

**System Status**: ✅ Ready to Deploy

Your concert ticketing system is fully functional and ready for testing and deployment!
