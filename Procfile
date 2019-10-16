web: gunicorn --worker-class eventlet -w 1 --log-file=- server:app
release: python manage.py db upgrade 