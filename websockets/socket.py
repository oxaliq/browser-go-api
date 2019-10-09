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