# 🔧 Render Configuration Quick Reference

## Essential Settings for Render Dashboard

### Web Service Configuration
```yaml
Service Name: movieapp-lab10
Runtime: Python 3
Root Directory: MovieApp_LAB10  # ⚠️ CRITICAL - Must point to Django project
Build Command: ./build.sh
Start Command: gunicorn movieapp_lab10.wsgi:application
Instance Type: Free
```

### Required Environment Variables
```env
SECRET_KEY=django-insecure-example-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=movieappv2-lab10.onrender.com,*.onrender.com
CSRF_TRUSTED_ORIGINS=https://movieappv2-lab10.onrender.com
```

### Optional Database (PostgreSQL)
```env
DATABASE_URL=postgresql://user:password@host:port/database
```

## File Requirements Checklist
- ✅ `build.sh` - Render build script
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python 3.11.10
- ✅ `movieapp_lab10/wsgi.py` - WSGI application
- ✅ `movieapp_lab10/settings.py` - Production settings

## Default Credentials (Change in Production)
```
Admin Username: admin@example.com
Admin Password: adminpass123
```

## Live URLs After Deployment
- App: `https://movieappv2-lab10.onrender.com`
- Admin: `https://movieappv2-lab10.onrender.com/admin/`
- Movies: `https://movieappv2-lab10.onrender.com/movies/`

## Troubleshooting
1. **Root Directory**: Must be `MovieApp_LAB10` (not repository root)
2. **Build Fails**: Check build.sh permissions and requirements.txt
3. **Static Files**: Automatically handled by WhiteNoise
4. **Database**: SQLite3 auto-created, no DATABASE_URL needed