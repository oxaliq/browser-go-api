from flask import Blueprint

room = Blueprint('rooms', __name__)

@room.route('/<int:room_id>')
def func():
    pass