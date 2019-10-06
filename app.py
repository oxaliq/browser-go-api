import os
from database import db, ma

from flask import Flask

from configuration.config import DevelopmentConfig

from flask_bcrypt import Bcrypt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    ma.init_app(app)
    return app

bcrypt = Bcrypt(create_app())