#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist (only if none exists)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Populate movies if database is empty (check first)
echo "from movie.models import Movie; Movie.objects.exists() or __import__('os').system('python manage.py populate_movies')" | python manage.py shell