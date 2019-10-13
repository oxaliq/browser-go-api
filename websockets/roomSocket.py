from app import socketio
from flask_socketio import send, emit, join_room, leave_room
import json
from models.Game import Game
from models.User import User, user_schema

def join_room_notice(room):
    @socketio.on('join room', namespace=f'/{room}')
    def connect_room(message):
        print(f'connected with ${message}')
        emit('connected', {'roomspace': f'/{room}'})

def new_game_notice(room, game):
    print('sending new game notice')
    socketio.emit('new game', game, broadcast=True, namespace=f'/{room}')


def new_room_notice(room):
    socketio.emit('new room', room, broadcast=True)

def join_game_notice(game_id, user):
    @socketio.on('join game')
    def handle_join_game(data):
        print(data)
        game_id = data['game']
        user_id = data['user']
        game = Game.query.filter_by(id=game_id).first()
        print('join game')
        print(game)
        print(game['player_black'])
        join_room(game_id)
        if not game['player_black']:
            game['player_black'] = user
            user = user_schema.dumps(User.query.filter_by(id=user_id).first())
            emit('new player', {'black': user}, broadcast=True)
        emit('join game', data, room=f'game')
