from app import create_app, db, socketio

# Blueprints
from api.api import api
from auth.auth import auth

import configuration.models_mount
from flask_migrate import Migrate



if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(api)
    app.register_blueprint(auth)
    migrate = Migrate(app, db)
    socketio.run(app)