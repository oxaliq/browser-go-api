from app import socketio
from flask_socketio import send, emit

@socketio.on('connect')
def handle_connection():
    print('''
    
    wow, there was a socketio connection!
    
    cool
    ''')
    emit('message', {'data':'connection'}, broadcast=True)

@socketio.on('message')
def handle_message(message):
    print(message)
    emit('init namespace', {'namespace':'newroom'})

@socketio.on('connect', namespace='/newroom')
def handle_connection():
    print('''

    look cool a namespaced socketio connection!

    ''')

def join_room_notice(room):
    @socketio.on('connect', namespace=f'/{room}')
    def handle_connection():
        print(f'joined room at {room}')
        emit('join room', {'roomspace': f'{room}'})
    @socketio.on('join room', namespace=f'/{room}')
    def connect_room(message):
        print(f'connected with ${message}')
        emit('connected', {'roomspace': f'/{room}'})

def new_game_notice(room, game):
    @socketio.on('connect', namespace=f'/{room}')
    def emit_game(game):
        pass


def new_room_notice(room):
    socketio.emit('new room', room, broadcast=True)

# @socketio.on
# def room_socket(roomspace):
#     pass