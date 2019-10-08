from flask import Blueprint, request, jsonify, session
from .users.user_endpoint import UserEndpoint
from .users.room_endpoint import RoomEndpoint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/home', methods=['GET'])
def api_home():
    response = {"message": "home page"}
    return jsonify(response)

@api.route('/users', methods=['GET'])
def api_get_users():
    return jsonify(UserEndpoint.users())

@api.route('/user', methods=['GET'])
def api_get_user():
    return jsonify(UserEndpoint.user())

@api.route('/rooms', methods=['GET'])
def api_get_rooms():
    return RoomEndpoint.get_rooms()

@api.route('/room', methods=['GET'])
def api_get_room():
    return RoomEndpoint.get_room()

# protected route
@api.route('/room', methods=['POST'])
def api_post_room():
    return pass