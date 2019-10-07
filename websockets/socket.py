from app import socketio
from flask_socketio import send, emit

@socketio.on('connect')
def handle_connection():
    print('''
    
    wow, there was a socketio connection!
    
    cool
    ''')
    send({'data':'connection'})

@socketio.on('message')
def handle_message(message):
    print(message)
    emit('message return', {'data':'a message was sent'})