from app import create_app, db

# Blueprints
from api.api import register_api_endpoints
from auth.auth import auth

# Web sockets
from websockets.socket import socketio 

import configuration.models_mount
from flask_migrate import Migrate

from flask import Blueprint, jsonify

server = Blueprint('server', __name__, url_prefix='/')

@server.route('/', methods=['GET'])
def api_home():
    response = {"message": "hello world"}
    return jsonify(response)

if __name__ == '__main__':
    app = create_app()
    register_api_endpoints(app)
    app.register_blueprint(server)
    migrate = Migrate(app, db)
    socketio.run(app, debug=True)
    
def run():
    app = create_app()
    register_api_endpoints(app)
    app.register_blueprint(server)
    migrate = Migrate(app, db)
    socketio.run(app, debug=False)
