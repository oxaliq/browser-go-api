import os
from database import db, ma

from flask import Flask

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# ! Environment Variable
# TODO change to os.getenv('CONFIGURATION')
# TODO export CONFIGURATION='configuration.config.ProductionConfig'
app.config.from_object('configuration.config.DevelopmentConfig')

# ! Environment Variable
# TODO change to os.getenv('ALLOWED_ORIGIN')
# TODO export ALLOWED_ORIGIN= whatever the react server is
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")

def create_app():
    CORS(app, resources={
        r"/api/*": {"origins": "http://localhost:3000"},
        r"/auth/*": {"origins": "http://localhost:3000"},
    })
    db.init_app(app)
    ma.init_app(app)
    return app
