from flask import Blueprint, request, jsonify, session
from models.User import User, user_schema, users_schema
from models.GameRoom import GameRoom, rooms_schema, room_schema
from models.Game import Game, games_schema
from database import db
from ..decorators import jwt_required
from websockets.roomSocket import new_room_notice, join_room_notice

api_rooms = Blueprint('api_rooms', __name__, url_prefix='/api/rooms')

@api_rooms.route('/<room_id>', methods=['GET'])
def get_room(room_id):
    print(room_id)
    games = Game.query.filter_by(game_room=room_id).all()
    response = games_schema.dumps(games)
    join_room_notice(room_id)
    return jsonify(response)

@api_rooms.route('/', methods=['GET'])
def get_rooms():
    rooms = GameRoom.query.all()
    response = rooms_schema.dumps(rooms)
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
        }
        new_room_notice(room_schema.dumps(room))
        return jsonify(response), 201
    except Exception as e:
        print(e)
        print(e.__dict__)
        response = {
            'status': 'fail',
            'message': 'There was an error. Please try again.'
        }
        return jsonify(response), 401