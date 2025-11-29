#!/usr/bin/env python
"""
Render Deployment Validation Script
Checks if the Django project is ready for Render deployment
IMPORTANT: This script assumes you're in the MovieApp_LAB10/ directory (Django project root)
For Render deployment, set Root Directory to 'MovieApp_LAB10' in your web service settings
"""
import os
import sys
from pathlib import Path

def check_file_exists(file_path, description):
    """Check if a file exists and print status"""
    if os.path.exists(file_path):
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description}: {file_path} (MISSING)")
        return False

def check_requirements():
    """Check if requirements.txt has necessary packages"""
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
            required_packages = ['Django', 'gunicorn', 'psycopg2-binary', 'whitenoise', 'python-decouple']
            missing_packages = []
            
            for package in required_packages:
                if package.lower() not in content.lower():
                    missing_packages.append(package)
            
            if missing_packages:
                print(f"❌ Missing packages in requirements.txt: {', '.join(missing_packages)}")
                return False
            else:
                print("✅ All required packages found in requirements.txt")
                return True
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def check_settings():
    """Check if settings.py is configured for production"""
    try:
        settings_path = Path('movieapp_lab10/settings.py')
        with open(settings_path, 'r') as f:
            content = f.read()
            
            checks = [
                ('python-decouple import', 'from decouple import config' in content),
                ('ALLOWED_HOSTS configuration', 'ALLOWED_HOSTS = config(' in content),
                ('WhiteNoise middleware', 'whitenoise.middleware.WhiteNoiseMiddleware' in content),
                ('Database URL configuration', 'DATABASE_URL' in content),
                ('Static files root', 'STATIC_ROOT' in content),
            ]
            
            all_good = True
            for check_name, condition in checks:
                if condition:
                    print(f"✅ {check_name}")
                else:
                    print(f"❌ {check_name}")
                    all_good = False
            
            return all_good
    except FileNotFoundError:
        print("❌ settings.py not found")
        return False

def main():
    """Main validation function"""
    print("🚀 Render Deployment Readiness Check")
    print("=" * 40)
    
    all_checks_passed = True
    
    # File existence checks
    files_to_check = [
        ('requirements.txt', 'Requirements file'),
        ('runtime.txt', 'Python runtime specification'),
        ('build.sh', 'Build script'),
        ('manage.py', 'Django management script'),
        ('movieapp_lab10/settings.py', 'Django settings'),
        ('movieapp_lab10/wsgi.py', 'WSGI application'),
        ('RENDER_DEPLOYMENT.md', 'Deployment guide'),
        ('render.env.example', 'Environment variables example'),
    ]
    
    print("\n📁 File Structure Check:")
    for file_path, description in files_to_check:
        if not check_file_exists(file_path, description):
            all_checks_passed = False
    
    print("\n📦 Dependencies Check:")
    if not check_requirements():
        all_checks_passed = False
    
    print("\n⚙️ Settings Configuration Check:")
    if not check_settings():
        all_checks_passed = False
    
    print("\n" + "=" * 40)
    if all_checks_passed:
        print("🎉 SUCCESS: Your project is ready for Render deployment!")
        print("\nNext steps:")
        print("1. Push your code to GitHub")
        print("2. Follow the steps in RENDER_DEPLOYMENT.md")
        print("3. Set up PostgreSQL database on Render")
        print("4. Configure environment variables")
        print("5. Deploy your web service")
    else:
        print("⚠️  WARNING: Some issues need to be resolved before deployment")
        print("Please fix the issues marked with ❌ above")
    
    return 0 if all_checks_passed else 1

if __name__ == '__main__':
    sys.exit(main())