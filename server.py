from app import create_app, db

# Blueprints
from api.api import register_api_endpoints
from auth.auth import auth

# Web sockets
from websockets.socket import socketio

import configuration.models_mount
from flask_migrate import Migrate



if __name__ == '__main__':
    app = create_app()
    register_api_endpoints(app)
    migrate = Migrate(app, db)
    socketio.run(app, debug=True)