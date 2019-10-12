from app import socketio
from flask_socketio import send, emit, join_room, leave_room
import json

# ! Basic Connection
@socketio.on('connect')
def handle_connection():
    print('''
    
    wow, there was a socketio connection!
    
    cool
    ''')
    emit('message', {'data':'connection'}, broadcast=True)

@socketio.on('send message')
def handle_message(message):
    print(message)
    emit('init namespace', {'namespace':'newroom'})

@socketio.on('connect', namespace='/newroom')
def handle_connection():
    print('''

    look cool a namespaced socketio connection!

    ''')
