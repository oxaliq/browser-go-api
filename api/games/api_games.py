from flask import Blueprint, request, jsonify, session
from models.User import User, user_schema, users_schema
from models.GameRoom import GameRoom, rooms_schema, room_schema
from models.Game import Game
from database import db
from ..decorators import jwt_required
import jwt
import os
import json

api_games = Blueprint('api_games', __name__, url_prefix='/api/games')

@api_games.route('/', methods=['POST'])
@jwt_required()
def post_game():
    print('Hey it\'s a post request!')
    data = request.get_json()
    # TODO create decorator that returns user from header
    auth_header = request.headers.get('Authorization')
    user = jwt.decode(auth_header.split(" ")[1], os.environ.get('SECRET_KEY'))['user']
    print(user)
    print('data')
    print(data)
    user_id = json.loads(user)['id']
    try:
        game = Game(
            name = data['name'],
            description = data['description'],
            board_size = data['boardSize'],
            game_room = data['gameRoom'],
            player_white = user_id
        )
        print(game)
        db.session.add(game)
        print('game added')
        db.session.commit()
        print('game')
        print(game)
        response = {
            'status': 'success',
            'message': 'Game created',
            'game': game.id
            }
        return jsonify(response), 201
    except Exception as e:
        print('error')
        print(e)
        print(e.__dict__)
        response = {
            'status': 'fail',
            'message': 'There was an error. Please try again.'
        }
        return jsonify(response), 401