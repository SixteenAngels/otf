# Enhanced Ticketing System API

Complete API documentation for Concert Ticket QR System.

## Base URL
```
http://localhost:8000/api
```

## Authentication
Include JWT token in Authorization header:
```
Authorization: Bearer YOUR_TOKEN
```

---

## 🔐 Authentication Endpoints

### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePassword123!",
  "role": "viewer"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "role": "viewer",
  "is_active": true,
  "created_at": "2024-01-17T10:00:00",
  "updated_at": "2024-01-17T10:00:00"
}
```

### Login
```http
POST /auth/login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "SecurePassword123!"
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "role": "viewer",
    "is_active": true,
    "created_at": "2024-01-17T10:00:00",
    "updated_at": "2024-01-17T10:00:00"
  }
}
```

---

## 🎭 Concert Endpoints

### List All Concerts
```http
GET /concerts/
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "name": "Taylor Swift Concert",
    "date": "2024-06-15T20:00:00",
    "venue": "Madison Square Garden",
    "description": "The Eras Tour",
    "created_at": "2024-01-17T10:00:00"
  }
]
```

### Get Concert Details
```http
GET /concerts/{concert_id}
```

### Create Concert (Admin Only)
```http
POST /concerts/
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "name": "Taylor Swift Concert",
  "date": "2024-06-15T20:00:00",
  "venue": "Madison Square Garden",
  "description": "The Eras Tour"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "name": "Taylor Swift Concert",
  "date": "2024-06-15T20:00:00",
  "venue": "Madison Square Garden",
  "description": "The Eras Tour",
  "created_at": "2024-01-17T10:00:00"
}
```

---

## 🎫 Ticket Endpoints

### Generate New Ticket (Admin Only)
```http
POST /tickets/create/{concert_id}
Authorization: Bearer YOUR_TOKEN
```

**Response** (201 Created):
```json
{
  "id": 1,
  "concert_id": 1,
  "ticket_number": "ABC123DEF456",
  "qr_code_data": "{\"ticket_id\": 1, \"ticket_number\": \"ABC123DEF456\", \"concert_id\": 1}",
  "status": "created",
  "buyer_name": null,
  "buyer_email": null,
  "price": null,
  "sold_at": null,
  "created_at": "2024-01-17T10:00:00",
  "updated_at": "2024-01-17T10:00:00"
}
```

### Get Ticket
```http
GET /tickets/{ticket_id}
```

### Get Ticket by Number
```http
GET /tickets/number/{ticket_number}
```

### Mark Ticket as Sold (Admin Only)
```http
POST /tickets/{ticket_id}/mark-sold
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "buyer_name": "John Doe",
  "buyer_email": "john@example.com",
  "price": 150.00
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "concert_id": 1,
  "ticket_number": "ABC123DEF456",
  "qr_code_data": "{...}",
  "status": "sold",
  "buyer_name": "John Doe",
  "buyer_email": "john@example.com",
  "price": 150.00,
  "sold_at": "2024-01-17T10:30:00",
  "created_at": "2024-01-17T10:00:00",
  "updated_at": "2024-01-17T10:30:00"
}
```

### List Concert Tickets
```http
GET /tickets/concert/{concert_id}
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "concert_id": 1,
    "ticket_number": "ABC123DEF456",
    "status": "sold",
    "buyer_name": "John Doe",
    "price": 150.00,
    ...
  }
]
```

---

## 📍 Scan Endpoints

### Record Scan (Scanner/Admin Only)
Records a ticket scan and updates the ticket's status based on the scan type and user role.

- **Verification users** (`verify*` username) can only scan a ticket once to mark it as `attended`.
- **Sales/Admin users** can scan tickets multiple times with different scan types (`sale`, `attendance`).

```http
POST /scans/
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "ticket_id": 1,
  "scan_type": "attendance",
  "location": "Gate 1",
  "notes": "Scanned at main entrance"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "ticket_id": 1,
  "scan_type": "attendance",
  "scanned_at": "2024-06-15T20:15:00",
  "scanner_id": 1,
  "location": "Gate 1",
  "notes": "Scanned at main entrance"
}
```

### Get Ticket Scans
```http
GET /scans/ticket/{ticket_id}
Authorization: Bearer YOUR_TOKEN
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "ticket_id": 1,
    "scan_type": "entry_check",
    "scanned_at": "2024-06-15T20:10:00",
    "scanner_id": 1,
    "location": "Gate 1",
    "notes": null
  },
  {
    "id": 2,
    "ticket_id": 1,
    "scan_type": "attendance",
    "scanned_at": "2024-06-15T20:15:00",
    "scanner_id": 1,
    "location": "Gate 1",
    "notes": "Confirmed attendance"
  }
]
```

### Get Attendance Statistics
```http
GET /scans/concert/{concert_id}/attendance
Authorization: Bearer YOUR_TOKEN
```

**Response** (200 OK):
```json
{
  "concert_id": 1,
  "total_sold": 1000,
  "total_attended": 950,
  "attendance_rate": "95.0%"
}
```

---

## 💰 Refund Endpoints

### Request Refund
```http
POST /refunds/request
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "ticket_id": 1,
  "reason": "Cannot attend due to illness",
  "amount": 150.00,
  "notes": "Medical emergency"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "ticket_id": 1,
  "user_id": 1,
  "reason": "Cannot attend due to illness",
  "amount": 150.00,
  "status": "pending",
  "notes": "Medical emergency",
  "requested_at": "2024-01-17T10:00:00",
  "processed_at": null,
  "created_at": "2024-01-17T10:00:00",
  "updated_at": "2024-01-17T10:00:00"
}
```

### List Refunds (Admin Only)
```http
GET /refunds/
Authorization: Bearer YOUR_TOKEN
```

### Approve Refund (Admin Only)
```http
POST /refunds/{refund_id}/approve
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "notes": "Approved - Full refund issued"
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "status": "approved",
  "notes": "Approved - Full refund issued",
  "processed_at": "2024-01-17T10:30:00",
  ...
}
```

### Reject Refund (Admin Only)
```http
POST /refunds/{refund_id}/reject
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "notes": "Rejected - Concert too close to event date"
}
```

---

## 🔄 Transfer Endpoints

### Initiate Transfer
```http
POST /transfers/initiate
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

{
  "ticket_id": 1,
  "to_user_id": 2,
  "notes": "Giving to my friend"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "ticket_id": 1,
  "from_user_id": 1,
  "to_user_id": 2,
  "status": "pending",
  "notes": "Giving to my friend",
  "initiated_at": "2024-01-17T10:00:00",
  "completed_at": null,
  "created_at": "2024-01-17T10:00:00",
  "updated_at": "2024-01-17T10:00:00"
}
```

### Get Pending Transfers
```http
GET /transfers/pending
Authorization: Bearer YOUR_TOKEN
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "ticket_id": 1,
    "from_user_id": 1,
    "to_user_id": 2,
    "status": "pending",
    "notes": "Giving to my friend",
    ...
  }
]
```

### Accept Transfer
```http
POST /transfers/{transfer_id}/accept
Authorization: Bearer YOUR_TOKEN
```

**Response** (200 OK):
```json
{
  "id": 1,
  "status": "accepted",
  "completed_at": "2024-01-17T10:30:00",
  ...
}
```

### Reject Transfer
```http
POST /transfers/{transfer_id}/reject
Authorization: Bearer YOUR_TOKEN
```

**Response** (200 OK):
```json
{
  "id": 1,
  "status": "rejected",
  ...
}
```

---

## 📊 Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

## Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

Example:
```json
{
  "detail": "Ticket not found"
}
```

---

## 🔄 Scan Types

- `sale` - Stage 1: Seller confirms sale.
- `attendance` - Stage 2: Venue verifies attendance.

## 📋 Ticket Status Values

- `created` - Newly created, not sold.
- `sold` - Sold to a buyer.
- `verified` - Verified by a venue scanner (deprecated).
- `duplicate` - Scanned more than once.
- `attended` - Attended the event.
- `refunded` - Refund approved.
- `transferred` - Transferred to another user.

## 👥 User Roles

- `admin` - Full access, manages concerts and approves refunds
- `scanner` - Can scan tickets
- `viewer` - Read-only access

## 💾 Refund Status Values

- `pending` - Awaiting admin review
- `approved` - Approved by admin
- `rejected` - Rejected by admin
- `completed` - Refund processed

## 🔀 Transfer Status Values

- `pending` - Awaiting recipient acceptance
- `accepted` - Recipient accepted transfer
- `rejected` - Recipient rejected transfer
- `completed` - Transfer finalized

---

## 🧪 Example Workflow

### 1. Create Admin Account
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

### 2. Login
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "Admin123!"
  }'
```
*Save the access_token from response*

### 3. Create Concert
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

### 4. Generate Tickets
```bash
curl -X POST http://localhost:8000/api/tickets/create/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```
*Repeat to create multiple tickets*

### 5. Mark Ticket as Sold
```bash
curl -X POST http://localhost:8000/api/tickets/1/mark-sold \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "buyer_name": "John Doe",
    "buyer_email": "john@example.com",
    "price": 150.00
  }'
```

### 6. Scan Ticket (on event day)
```bash
curl -X POST http://localhost:8000/api/scans/ \
  -H "Authorization: Bearer SCANNER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket_id": 1,
    "scan_type": "attendance",
    "location": "Gate 1"
  }'
```

### 7. View Attendance Stats
```bash
curl http://localhost:8000/api/scans/concert/1/attendance \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 📚 Additional Resources

- Interactive Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Backend README: `backend/README.md`
- Frontend README: `frontend/README.md`
