import os
from database import db, ma, bcrypt

from flask import Flask

from flask_migrate import Migrate

from flask_cors import CORS

# Blueprints
from api.api import api
from auth.auth import auth

import config.models_mount

def create_app():
    app = Flask(__name__)
    bcrypt(app)
    CORS(app)
    app_settings = os.getenv(    
        'APP_SETTINGS',
        'config.config.DevelopmentConfig'
    )

    app.config.from_object(app_settings)
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api)
    app.register_blueprint(auth)
    migrate = Migrate(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8000, debug=True)