# Railway Deployment Guide

## Step 1: Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub account (easiest option)
3. Authorize Railway to access your GitHub repositories

## Step 2: Create PostgreSQL Database on Railway
1. Dashboard → Create New → Database → PostgreSQL
2. Wait for database to initialize (~1 minute)
3. Click on PostgreSQL service
4. Go to **Variables** tab
5. Copy the `DATABASE_URL` (starts with `postgresql+asyncpg://`)
6. Save this - you'll need it for backend deployment

### Important Database Setup
After PostgreSQL is created, you need to run migrations:
- The migrations will automatically run when backend starts (Alembic)
- Or manually: Connect to database and run migration scripts

## Step 3: Deploy Backend
1. Dashboard → Create New → GitHub Repo
2. Select your concert-ticket repository
3. Select the `main` branch
4. Choose deployment settings:
   - **Root Directory**: `backend`
   - **Add Environment Variables**:
     - `DATABASE_URL`: Paste from Step 2
     - `SECRET_KEY`: Generate a secure random string (use Python: `python -c "import secrets; print(secrets.token_urlsafe(32))"`)
     - `ENV`: `production`

5. Click **Deploy**
6. Wait for deployment to complete (2-3 minutes)
7. Copy the generated backend URL (looks like: `https://concert-backend-production.railway.app`)

### Backend Deployment Checklist
- [ ] PostgreSQL database created and URL copied
- [ ] Backend repository connected to Railway
- [ ] Environment variables set (DATABASE_URL, SECRET_KEY, ENV)
- [ ] Backend deployed successfully
- [ ] Backend health check passing (visit `/docs` on backend URL)

## Step 4: Deploy Frontend
1. Dashboard → Create New → GitHub Repo
2. Select the same concert-ticket repository
3. Select the `main` branch
4. Choose deployment settings:
   - **Root Directory**: `frontend`
   - **Add Environment Variables**:
     - `REACT_APP_API_URL`: Paste your backend URL from Step 3
     - `NODE_ENV`: `production`
   - **Start Command**: `npm start` (if custom needed)
   - **Build Command**: `npm run build` (if custom needed)

5. Click **Deploy**
6. Wait for deployment (2-3 minutes)
7. Copy the generated frontend URL (looks like: `https://concert-frontend-production.railway.app`)

### Frontend Deployment Checklist
- [ ] Backend URL obtained from Step 3
- [ ] Frontend repository connected to Railway
- [ ] REACT_APP_API_URL environment variable set to backend URL
- [ ] Frontend deployed successfully
- [ ] Frontend loads and can reach backend

## Step 5: Run Database Migrations
Once backend is deployed:

1. Open your PostgreSQL service in Railway
2. Click the **Connect** button
3. Copy the connection string
4. From your local machine, connect and run migrations:
   ```bash
   cd backend
   # Install Alembic if not already
   pip install alembic
   
   # Set DATABASE_URL and run migration
   $env:DATABASE_URL = "postgresql://..." # Use Railway PostgreSQL connection string
   alembic upgrade head
   ```

Alternatively, migrations run automatically on first backend startup if configured.

## Step 6: Test Your Deployment

### Test Backend
```bash
# Check API is running
curl https://your-backend-url.railway.app/docs

# Test login endpoint
curl -X POST https://your-backend-url.railway.app/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "otf",
    "password": "cows12"
  }'
```

### Test Frontend
1. Visit your frontend URL
2. Login with credentials:
   - Admin: `otf` / `cows12`
   - Sales: `sales1` / (check seeded_accounts.txt for password)
   - Verify: `verify1` / (check seeded_accounts.txt for password)
3. Test QR scanning functionality
4. Try admin dashboard (delete tickets, generate QRs)

## Step 7: Configure Domain (Optional)
1. Railway Dashboard → Your Project
2. Select Frontend service
3. Click **Settings**
4. Under **Domains**, add custom domain or use Railway subdomain

## Step 8: Enable CORS for Production
Your backend CORS is currently set to localhost. Update it:

**File**: `backend/app/main.py`
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.railway.app"],  # Replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Troubleshooting

### Backend won't start
- Check logs in Railway dashboard
- Verify DATABASE_URL format is correct
- Ensure all environment variables are set
- Check migrations ran successfully

### Frontend can't reach backend
- Verify REACT_APP_API_URL is set correctly
- Check backend is responding (visit `/docs`)
- Check browser console for CORS errors
- Verify backend CORS includes your frontend URL

### Database connection failed
- Test PostgreSQL is running in Railway
- Verify DATABASE_URL in backend service
- Check IP whitelist (Railway handles this)
- Verify user credentials in connection string

### QR codes not generating
- Ensure Pillow is installed (check requirements.txt)
- Check backend logs for qrcode library errors
- Verify base64 encoding in response

### Login returns 401
- Verify users were seeded in production database
- Check SECRET_KEY matches between login and token verification
- Ensure argon2-cffi is installed on backend

## Production Checklist
- [ ] PostgreSQL database created and running
- [ ] Backend deployed with correct environment variables
- [ ] Frontend deployed with correct backend URL
- [ ] Database migrations completed
- [ ] Users seeded (or create via API)
- [ ] Login flow tested
- [ ] QR generation tested
- [ ] Scanner functionality tested
- [ ] Admin delete/download functions tested
- [ ] Role-based access control verified
- [ ] CORS configured for production domain
- [ ] Monitoring/logging enabled (optional)
- [ ] Backups configured (optional)

## Monitoring & Maintenance
- Monitor Railway dashboard for deployment logs
- Set up error notifications
- Keep dependencies updated
- Regular database backups
- Monitor usage and costs

## Support
- Railway Documentation: https://docs.railway.app
- FastAPI Deployment: https://fastapi.tiangolo.com/deployment/
- React Build: https://create-react-app.dev/deployment/

---
Once deployment is complete, your system will be live and accessible to users!
