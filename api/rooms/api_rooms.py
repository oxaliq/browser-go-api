from flask import Blueprint, request, jsonify, session
from models.User import User, user_schema, users_schema
from models.GameRoom import GameRoom
from database import db
from ..decorators import jwt_required

api_rooms = Blueprint('api_rooms', __name__, url_prefix='/api/rooms')

@api_rooms.route('/<room_id>', methods=['GET'])
def get_room():
    pass

@api_rooms.route('/', methods=['GET'])
def get_rooms():
    response = {"status" : "success"}
    return jsonify(response)

# protected route
@api_rooms.route('/', methods=['POST'])
@jwt_required()
def post_room():
    print('Hey it\'s a POST request')
    data = request.get_json()
    print(data)
    try:
        room = GameRoom(
        name = data['name'],
        description = data['description'],
        #  TODO add support for private rooms and multiple languages
        # private = data['private'],
        # language = data['language']
        )
        db.session.add(room)
        db.session.commit()
        response = {
            'status': 'success',
            'message': 'Succesfully registered.',
            'gameRoom': room.id
        }
        return jsonify(response), 201
    except Exception as e:
        print(e.__dict__)
        response = {
            'status': 'fail',
            'message': 'There was an error. Please try again.'
        }
        return jsonify(response), 401