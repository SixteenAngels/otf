# Concert Ticket QR Code Management System

A complete full-stack system for managing concert tickets using QR codes. Built with FastAPI (backend), React (frontend), and PostgreSQL (database). Features include user authentication, ticket generation, QR scanning for attendance tracking, refund management, and ticket transfers.

## 🎯 Features

### Core Functionality
- ✅ **User Authentication**: JWT-based auth with role-based access control
- ✅ **Concert Management**: Create and organize concert events
- ✅ **Ticket Generation**: Auto-generate unique tickets with QR codes
- ✅ **QR Scanning**: Real-time QR code scanning from mobile/web
- ✅ **Sales Tracking**: Track sold tickets with buyer information
- ✅ **Attendance Tracking**: Scan tickets to verify attendance
- ✅ **Attendance Analytics**: Real-time attendance statistics

### Advanced Features
- ✅ **Refund Management**: Request and approve ticket refunds
- ✅ **Ticket Transfers**: Transfer tickets between users with approval
- ✅ **Role-Based Access**: Admin, Scanner, Viewer roles
- ✅ **Database Migrations**: Version control with Alembic
- ✅ **Async Operations**: Built on async/await for high performance
- ✅ **Docker Support**: Full Docker Compose setup for easy deployment

## 📋 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Concert Ticket System                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────┐         ┌──────────────────────┐  │
│  │  React Frontend      │         │  FastAPI Backend     │  │
│  │  - QR Scanner        │         │  - JWT Auth          │  │
│  │  - Admin Dashboard   │◄───────►│  - REST API          │  │
│  │  - Ticket Manager    │         │  - QR Generation     │  │
│  │  - Refund Manager    │         │  - Scan Tracking     │  │
│  └──────────────────────┘         └──────────────────────┘  │
│           :8000                            :3000             │
│                                                               │
│                            │                                  │
│                            ▼                                  │
│                ┌──────────────────────────┐                  │
│                │   PostgreSQL Database    │                  │
│                │  (Neon.tech serverless) │                  │
│                └──────────────────────────┘                  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
concert-ticket-system/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── models/             # Database models
│   │   ├── routes/             # API endpoints
│   │   ├── schemas/            # Pydantic schemas
│   │   ├── utils/              # Utilities (QR, auth)
│   │   ├── database.py         # Async DB config
│   │   └── settings.py         # Configuration
│   ├── alembic/                # Database migrations
│   ├── main.py                 # Application entry
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Docker image
│   └── README.md               # Backend docs
│
├── frontend/                   # React application
│   ├── src/
│   │   ├── api/                # API client & endpoints
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── store/              # Zustand state
│   │   ├── App.jsx             # Main app
│   │   └── index.jsx           # Entry point
│   ├── public/                 # Static files
│   ├── package.json            # Node dependencies
│   ├── Dockerfile              # Docker image
│   ├── tailwind.config.js      # Tailwind config
│   └── README.md               # Frontend docs
│
├── docker-compose.yml          # Docker Compose setup
└── README.md                   # This file
```

## 🚀 Quick Start

### Option 1: Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Update .env with your Neon.tech credentials
alembic upgrade head
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

#### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm start
```

Frontend runs at: `http://localhost:3000`

### Option 2: Docker Compose

```bash
docker-compose up -d
```

This starts:
- PostgreSQL at `localhost:5432`
- Backend at `localhost:8000`
- Frontend at `localhost:3000`

To stop:
```bash
docker-compose down
```

## 🔧 Configuration

### Backend Environment Variables

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@host/db

# Environment
ENV=development

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend Environment Variables

```env
# API URL
REACT_APP_API_URL=http://localhost:8000
```

## 📚 Database Setup

### Using Neon.tech (Recommended)

1. Create account at [neon.tech](https://neon.tech)
2. Create a PostgreSQL database
3. Copy connection string
4. Update `.env` with connection string:
   ```
   DATABASE_URL=postgresql+asyncpg://neondb_owner:your_password@your_host/neondb
   ```

### Using Local PostgreSQL

1. Install PostgreSQL
2. Create database:
   ```sql
   CREATE DATABASE concert_tickets;
   ```
3. Update `.env`:
   ```
   DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/concert_tickets
   ```

### Run Migrations

```bash
cd backend
alembic upgrade head
```

## 👥 User Roles

| Role | Permissions |
|------|------------|
| **Admin** | Create concerts, manage tickets, approve refunds, view all data |
| **Scanner** | Scan tickets, view attendance stats |
| **Viewer** | View-only access, request refunds/transfers |

## 🔐 Authentication

### Register New User

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "securepass123",
    "role": "admin"
  }'
```

### Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "securepass123"
  }'
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "role": "admin",
    "is_active": true
  }
}
```

## 📱 API Examples

### Create Concert

```bash
curl -X POST http://localhost:8000/api/concerts/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Taylor Swift Concert",
    "date": "2024-06-15T20:00:00",
    "venue": "Madison Square Garden",
    "description": "The Eras Tour"
  }'
```

### Generate Ticket

```bash
curl -X POST http://localhost:8000/api/tickets/create/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Scan Ticket

```bash
curl -X POST http://localhost:8000/api/scans/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket_id": 1,
    "scan_type": "attendance",
    "location": "Gate 1"
  }'
```

### Get Attendance Stats

```bash
curl http://localhost:8000/api/scans/concert/1/attendance \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Response:
```json
{
  "concert_id": 1,
  "total_sold": 1000,
  "total_attended": 950,
  "attendance_rate": "95.0%"
}
```

## 🧪 Testing

### Backend Tests

```bash
cd backend
pip install pytest pytest-asyncio httpx
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## 🛠️ Development

### Backend Development

- **Hot Reload**: `uvicorn main:app --reload`
- **Debug**: Use VS Code debugger with Python extension
- **Linting**: Add pylint/black for code style

### Frontend Development

- **Hot Reload**: Built-in with `npm start`
- **Debugging**: Browser DevTools
- **Linting**: ESLint configured via Create React App

## 📦 Deployment

### Production Build

#### Backend
```bash
# Build Docker image
docker build -t concert-api:latest ./backend

# Push to registry
docker push concert-api:latest

# Deploy with Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### Frontend
```bash
# Build React app
cd frontend
npm run build

# Serve from web server (nginx, Apache, etc.)
```

### Environment Configuration

Set production environment variables:
- Strong `SECRET_KEY`
- Production database URL
- Appropriate CORS origins
- HTTPS enabled
- Rate limiting enabled

## 🐛 Troubleshooting

### Database Connection Failed
- Check DATABASE_URL format
- Verify database is running
- Check firewall/network access
- Test with: `psql <connection_string>`

### QR Scanner Not Working
- Allow camera permissions
- Use HTTPS in production
- Check browser compatibility
- Ensure good lighting

### API Returns 401 Unauthorized
- Token may be expired
- Refresh by re-logging in
- Check token in localStorage

### Frontend Can't Reach Backend
- Verify backend is running on correct port
- Check REACT_APP_API_URL
- Verify CORS is enabled
- Check network connectivity

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [React Documentation](https://react.dev)
- [SQLAlchemy Async](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Neon.tech Docs](https://neon.tech/docs)
- [Tailwind CSS](https://tailwindcss.com)

## 📝 License

This project is provided as-is for educational and commercial use.

## 🤝 Support

For issues, questions, or contributions:
1. Check existing documentation
2. Review API documentation at `/docs`
3. Check troubleshooting section above

## 🎯 Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Email notifications
- [ ] SMS reminders
- [ ] Payment integration
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] Dark mode
- [ ] Real-time notifications (WebSocket)

---

**Version**: 2.0.0  
**Last Updated**: January 2026  
**Status**: Production Ready
