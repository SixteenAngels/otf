# Railway Deployment Checklist

## ✅ Preparation Complete
- ✅ `psycopg2-binary` added to requirements.txt
- ✅ Backend configured for PostgreSQL in production
- ✅ `.env.production` file created for backend
- ✅ `.env.production` file created for frontend
- ✅ `railway.json` configuration created
- ✅ Settings updated to support both development and production

## 📋 Quick Steps to Deploy

### Step 1: Create GitHub Repository (if not already done)
```powershell
cd "c:\Users\Donfrass\Desktop\otf\qr code"
git init
git add .
git commit -m "Initial commit - Concert Ticket System"
git branch -M main
# Then create new repo on GitHub and push
```

### Step 2: Go to Railway.app
1. Visit https://railway.app
2. Sign up with GitHub (or sign in)
3. Authorize Railway access to your GitHub

### Step 3: Create PostgreSQL Database
1. Click **Create New → Database → PostgreSQL**
2. Wait for database to initialize
3. Click the PostgreSQL service
4. Go to **Variables** tab
5. Copy the `DATABASE_URL` value (full connection string)

### Step 4: Deploy Backend Service
1. **Create New → GitHub Repo**
2. Select your concert-ticket repository
3. **Root Directory**: `backend`
4. **Environment Variables** (Add):
   - `DATABASE_URL`: [Paste from Step 3]
   - `SECRET_KEY`: Generate random with: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
   - `ENV`: `production`
5. Click **Deploy**
6. Wait 2-3 minutes for deployment
7. **Copy your backend URL** from the service (Format: `https://concert-backend-xyz.railway.app`)

### Step 5: Deploy Frontend Service
1. **Create New → GitHub Repo**
2. Same repository
3. **Root Directory**: `frontend`
4. **Environment Variables** (Add):
   - `REACT_APP_API_URL`: [Paste your backend URL from Step 4]
   - `NODE_ENV`: `production`
5. Click **Deploy**
6. Wait 2-3 minutes
7. **Copy your frontend URL** (Format: `https://concert-frontend-xyz.railway.app`)

### Step 6: Verify Deployment
- Frontend URL should load login page
- Try logging in with:
  - Username: `otf`
  - Password: `cows12`
- Test QR scanner
- Test admin dashboard

## 📚 Additional Resources
- Full guide: [RAILWAY_DEPLOYMENT_GUIDE.md](RAILWAY_DEPLOYMENT_GUIDE.md)
- Live dashboard: https://railway.app/dashboard
- Railway docs: https://docs.railway.app

## 🔐 Production Credentials
### Test Users (from seeded_accounts.txt)
- **Admin**: 
  - Username: `otf`
  - Password: `cows12`
  
- **Sales Users**: sales1-sales10 (check seeded_accounts.txt)
- **Verify Users**: verify1-verify10 (check seeded_accounts.txt)

## 🚨 Important Notes
1. **Database Migrations**: Alembic migrations run automatically on backend startup
2. **First Login**: After deployment, the database tables will be created automatically
3. **Seed Data**: You need to seed users in production. Options:
   - Use the API to create users manually
   - Run seed script against production database
   - Load SQL directly via Railway PostgreSQL console

## 💡 Troubleshooting
If deployment fails:
1. Check Railway dashboard logs
2. Verify environment variables are set correctly
3. Ensure GitHub repository is public (or grant access)
4. Check that root directories are correct (backend/, frontend/)
5. Verify all dependencies in requirements.txt

## ✨ After Deployment
- Monitor Railway dashboard for errors
- Test all major features
- Consider setting up backups
- Enable monitoring/alerts (optional)
- Update DNS if using custom domain

---
**Status**: Ready for deployment on Railway
**Last Updated**: January 2026
