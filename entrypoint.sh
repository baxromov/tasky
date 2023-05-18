#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py create_user
python manage.py create_product 50
# Running gunicorn server with three workers
# Start Gunicorn processes
echo "Starting Gunicorn."

exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
