from models.User import User, user_schema, users_schema
from models.GameRoom import GameRoom
from flask import Blueprint, request, jsonify, session

api_rooms = Blueprint('api_rooms', __name__, url_prefix='/api/rooms')

@api_rooms.route('/<id>', methods=['GET'])
def get_room():
    pass

@api_rooms.route('/', methods=['GET'])
def get_rooms():
    response = {"status" : "success"}
    return jsonify(response)

# protected route
@api_rooms.route('/', methods=['POST'])
def post_room():
    pass