# 🚀 Render Deployment Guide for MovieApp LAB10

## Overview
This Django MovieApp is configured for easy deployment to **Render.com**, a modern cloud platform that automatically deploys from GitHub. The app uses **SQLite3 by default** (perfect for educational projects) with optional PostgreSQL support.

---

## 📋 Prerequisites

### 1. GitHub Repository
- Code must be pushed to GitHub
- **IMPORTANT**: Django project is in `MovieApp_LAB10/` subdirectory

### 2. Render Account
- Create free account at [render.com](https://render.com)
- Connect your GitHub account

---

## ⚙️ Quick Deployment Steps

### Step 1: Create Web Service on Render

1. **Go to Render Dashboard** → "New" → "Web Service"
2. **Connect Repository**: Select your GitHub repo
3. **Configure Service**:
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `movieapp-lab10` (or your preferred name) |
   | **Root Directory** | `MovieApp_LAB10` ⚠️ **CRITICAL** |
   | **Runtime** | `Python 3` |
   | **Build Command** | `./build.sh` |
   | **Start Command** | `gunicorn movieapp_lab10.wsgi:application` |
   | **Instance Type** | `Free` |

### Step 2: Environment Variables

Add these environment variables in Render:

```env
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=movieappv2-lab10.onrender.com,*.onrender.com
CSRF_TRUSTED_ORIGINS=https://movieappv2-lab10.onrender.com
```

**Generate Secret Key**: Use [djecrety.ir](https://djecrety.ir/) or Django shell

### Step 3: Deploy

1. Click **"Create Web Service"**
2. Render automatically builds and deploys
3. Monitor build logs for any issues

---

## 📊 Database Configuration

### SQLite3 (Default - Recommended for Educational Use)
- **No additional setup required**
- Database file created automatically
- Sample movies populated during build
- Perfect for demos and learning

### PostgreSQL (Optional - Production Use)
If you need PostgreSQL:

1. **Create PostgreSQL database** in Render
2. **Add environment variable**:
   ```env
   DATABASE_URL=postgresql://username:password@host:port/database
   ```
3. Redeploy the service

---

## 🔧 What Happens During Deployment

The `build.sh` script automatically:

1. ✅ Installs Python dependencies
2. ✅ Collects static files for CSS/JS
3. ✅ Runs database migrations
4. ✅ Creates admin user (`admin` / `admin`)
5. ✅ Populates 10 sample movies
6. ✅ Validates deployment readiness

---

## 👤 Default Login Credentials

After deployment, you can log in with:

```
Username: admin
Password: admin
```

**🔒 Security Note**: Change these credentials in production!

---

## 🌟 Features Available After Deployment

### User Features
- ✅ User registration with email
- ✅ Login/logout functionality  
- ✅ Browse movie collection
- ✅ Search movies by name/genre
- ✅ Add new movies (authenticated users)
- ✅ Edit existing movies
- ✅ Delete movies with confirmation

### Admin Features  
- ✅ Django admin interface at `/admin/`
- ✅ User management
- ✅ Movie management with filters
- ✅ Bulk operations

---

## 🔍 Troubleshooting

### Common Issues

#### "Build failed" Error
```bash
# Check Root Directory is set to: MovieApp_LAB10
# Verify build.sh is executable
```

#### Static Files Not Loading
```bash
# Ensure collectstatic runs in build.sh
# Check STATIC_ROOT in settings.py
```

#### Database Issues
```bash
# SQLite3: No action needed (auto-created)
# PostgreSQL: Verify DATABASE_URL format
```

#### Import Errors
```bash
# Ensure all requirements in requirements.txt
# Check Python version in runtime.txt
```

### Debug Steps

1. **Check Build Logs** in Render dashboard
2. **Verify Environment Variables** are set correctly
3. **Test Locally** with same configuration
4. **Run Validation**: `python validate_deployment.py`

---

## 📁 File Structure for Deployment

```
MovieAppV2_LAB10/              ← GitHub repository root
└── MovieApp_LAB10/           ← Django project (SET AS ROOT DIRECTORY)
    ├── build.sh              ← Render build script
    ├── requirements.txt      ← Python dependencies
    ├── runtime.txt           ← Python version
    ├── render.env.example    ← Environment template
    ├── manage.py            ← Django management
    ├── movieapp_lab10/      ← Django settings
    └── movie/               ← Main app
```

---

## 🎯 Render Dashboard URLs

After deployment, access your app:

- **Live App**: `https://movieappv2-lab10.onrender.com`
- **Admin**: `https://movieappv2-lab10.onrender.com/admin/`
- **Movies**: `https://movieappv2-lab10.onrender.com/movies/`

---

## 💡 Tips for Success

### Before Deployment
- ✅ Test locally with `DEBUG=False`
- ✅ Run `python validate_deployment.py`
- ✅ Ensure all requirements in `requirements.txt`
- ✅ Set proper `ALLOWED_HOSTS`

### After Deployment
- ✅ Change default admin password
- ✅ Test all CRUD operations
- ✅ Verify search functionality
- ✅ Check responsive design

### Performance
- ✅ Free tier: Spins down after inactivity
- ✅ First request may be slow (cold start)
- ✅ Consider upgrading for production use

---

## 🆘 Support Resources

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Django Deployment**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Project Validation**: Run `python validate_deployment.py`
- **Local Testing**: Follow README.md instructions

---

*🎬 Your MovieApp will be live and ready for users to browse, search, and manage movies!*