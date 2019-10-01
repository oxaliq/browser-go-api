from flask import Blueprint

game = Blueprint('games', __name__)

@game.route('/<int:game_id>')
def func():
    pass