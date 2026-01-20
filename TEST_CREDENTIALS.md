# Concert Ticket QR System - Test Credentials

## Deployment URLs
- **Frontend**: https://otf-production-7e0f.up.railway.app
- **Backend API**: https://otf.railway.app
- **Health Check**: https://otf.railway.app/health

## Test User Credentials

### Admin (Full Access)
| Username | Email | Password |
|----------|-------|----------|
| otf | admin@otf.com | cows12 |

### Sales Users (Stage 1 - Confirm ticket sale before handing out)
| # | Username | Email | Password |
|---|----------|-------|----------|
| 1 | sales1 | sales1@concert.com | vmpxJs |
| 2 | sales2 | sales2@concert.com | 0v5m7B |
| 3 | sales3 | sales3@concert.com | PXRPvS |
| 4 | sales4 | sales4@concert.com | zXfaX8 |
| 5 | sales5 | sales5@concert.com | no9LzA |
| 6 | sales6 | sales6@concert.com | fkRaMf |
| 7 | sales7 | sales7@concert.com | GlXaHW |
| 8 | sales8 | sales8@concert.com | MZvd6C |
| 9 | sales9 | sales9@concert.com | P5Q0PM |
| 10 | sales10 | sales10@concert.com | PxPove |

### Verify Users (Stage 2 - Verify at venue)
| # | Username | Email | Password |
|---|----------|-------|----------|
| 1 | verify1 | verify1@concert.com | kWYzRa |
| 2 | verify2 | verify2@concert.com | a7WMYT |
| 3 | verify3 | verify3@concert.com | IQnj28 |
| 4 | verify4 | verify4@concert.com | 6nGzr9 |
| 5 | verify5 | verify5@concert.com | yBWP8l |
| 6 | verify6 | verify6@concert.com | L9TDtv |
| 7 | verify7 | verify7@concert.com | SXQzc9 |
| 8 | verify8 | verify8@concert.com | S8dvXP |
| 9 | verify9 | verify9@concert.com | vlMEmz |
| 10 | verify10 | verify10@concert.com | BFnVZt |

## System Architecture

### Technologies
- **Frontend**: React with Tailwind CSS, Vite build
- **Backend**: FastAPI (Python), Uvicorn server
- **Database**: SQLite (automatic initialization on startup)
- **Password Hashing**: Argon2-cffi (secure, resistant to GPU attacks)
- **Authentication**: JWT Bearer tokens
- **QR Codes**: qrcode library (base64 PNG format)

### Features
1. **User Management**: Role-based access control (Admin, Sales, Verify)
2. **Concert Management**: Create and manage concerts
3. **Ticket Management**: Generate unique QR codes for each ticket
4. **Sales Workflow**: Sales users confirm ticket sales before distribution
5. **Venue Verification**: Verify users scan QR codes at venue (1-scan limit per ticket)
6. **Ticket Transfers**: Support ticket transfers between users
7. **Attendance Tracking**: Record attendance via QR code scans

### Database
- Automatically initialized on backend startup
- SQLite database file stored in container: `concert_tickets.db`
- Tables: users, concerts, tickets, scans, transfers

## Deployment Status
✅ Backend: Running and healthy
✅ Frontend: Deployed
✅ Database: Auto-initialized with all test users
✅ Authentication: Working with Argon2 password hashing

## API Endpoints (Examples)
- `POST /api/auth/login` - User login
- `GET /api/concerts/` - List concerts
- `POST /api/concerts/` - Create concert (admin only)
- `GET /api/tickets/concert/{id}` - List tickets for concert
- `GET /api/tickets/{id}/qr-code` - Get QR code for ticket
- `POST /api/scans/` - Record ticket scan (verify only)
- `GET /api/scans/concert/{id}/attendance` - Get attendance for concert

## Notes
- All passwords are 6 characters (random alphanumeric)
- Admin can create additional users via the frontend
- QR codes are stored as base64-encoded PNG images
- Tickets can only be scanned once at the venue (automatic limit enforcement)
