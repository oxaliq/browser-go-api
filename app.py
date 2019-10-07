import os
from database import db, ma

from flask import Flask

from configuration.config import DevelopmentConfig

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(DevelopmentConfig)
socketio = SocketIO(app)

def create_app():
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"},
    r"/auth/*": {"origins": "http://localhost:3000"}})
    db.init_app(app)
    ma.init_app(app)
    return app
