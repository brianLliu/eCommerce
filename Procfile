release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn commerce.wsgi --log-file=-
