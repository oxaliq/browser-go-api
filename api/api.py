from flask import Blueprint, request, jsonify, session
from .users.user_endpoint import UserEndpoint
from app import socketio
from flask_socketio import emit

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/home', methods=['GET'])
def api_home():
    response = {"message": "home page"}
    return jsonify(response)

@api.route('/users')
def api_users():
    return jsonify(UserEndpoint.users())

@api.route('/user')
def api_user():
    return jsonify(UserEndpoint.user())

@socketio.on('connect')
def handle_connection():
    print('connected')
    socketio.emit('connect', payload={'data':'connection'})

@socketio.on('message')
def handle_message(message):
    print(message)
    emit('message return', {'data':'a message was sent'})