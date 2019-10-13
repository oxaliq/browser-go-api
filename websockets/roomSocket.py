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

def join_game_notice(game):
    print('join game')
    print(game)
    black = user_schema.dumps(User.query.filter_by(id=game.player_black).first())
    white = user_schema.dumps(User.query.filter_by(id=game.player_white).first())
    room_id = game.game_room
    game_id = game.id
    print(black)
    @socketio.on('join game', namespace=f'/{room_id}')
    def handle_join_game(data):
        print('emit join game')
        join_room(game_id)
        emit('join game', {'black': black, 'white': white}, broadcast=True)
