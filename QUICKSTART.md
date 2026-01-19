# Quick Start Guide

## Prerequisites
- Python 3.10+
- Node.js 16+
- PostgreSQL (or Neon.tech account)
- Git

## 1-Minute Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Update `.env` with your database URL:
```
DATABASE_URL=postgresql+asyncpg://user:password@host/db
```

Run migrations and start:
```bash
alembic upgrade head
uvicorn main:app --reload
```

✅ Backend ready at `http://localhost:8000`

### Frontend
```bash
cd frontend
npm install
npm start
```

✅ Frontend ready at `http://localhost:3000`

### Create First Admin User (via API)

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "email": "admin@example.com",
    "password": "Admin123!",
    "role": "admin"
  }'
```

### Login in Frontend
1. Go to `http://localhost:3000/login`
2. Enter username: `admin`
3. Enter password: `Admin123!`
4. Click "Sign in"

## Using Docker

One command to start everything:

```bash
docker-compose up -d
```

Then access:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

## Next Steps

1. **Create a Concert** (Admin Dashboard)
   - Click "Create Concert" button
   - Fill in details (name, date, venue)

2. **Generate Tickets** (Backend API)
   ```bash
   curl -X POST http://localhost:8000/api/tickets/create/1 \
     -H "Authorization: Bearer YOUR_TOKEN"
   ```

3. **Scan Tickets** (Scanner Page)
   - Point camera at QR code
   - Confirm scan type
   - View attendance stats

## Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/auth/login` | POST | User login |
| `/api/concerts/` | GET/POST | List/Create concerts |
| `/api/tickets/create/{id}` | POST | Generate ticket |
| `/api/scans/` | POST | Record scan |
| `/api/refunds/request` | POST | Request refund |
| `/api/transfers/initiate` | POST | Transfer ticket |

## Troubleshooting

**Backend won't start**: Check DATABASE_URL in .env

**Frontend shows 401**: Clear localStorage and re-login

**Scanner not working**: Check camera permissions and use HTTPS

**Database migration fails**: Verify database exists and is accessible

## Full Documentation

- Backend: `backend/README.md`
- Frontend: `frontend/README.md`
- Main: `README.md`
