from app import socketio
from flask_socketio import send, emit, join_room, leave_room
import json

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
    def return_join_game_notice(data):
        game = data['game']
        join_room(game)
        emit('join game', data, room=f'game')
