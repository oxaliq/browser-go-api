web: gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker --log-file=- server:app
release: python manage.py db upgrade 