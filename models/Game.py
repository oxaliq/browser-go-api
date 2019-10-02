from ..app import db, ma
import enum

class Players(enum.Enum):
    BLACK = "The player taking black stones"
    WHITE = "The player taking white stones"

class WinType(enum.Enum):
    DRAW = "The game is a draw"
    RESIGN = "The game ended in resignation"
    SCORE = "The game ended by counting points"
    TIME = "The game ended in loss by time out"
    VOID = "The game was suspended"

class Game(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    komi = db.Column(db.Decimal(2,1))
    handicap = db.Column(db.Integer)
    board_size = db.Column(db.Integer)
    win_type = db.Column(db.Enum(WinType))
    winner = db.Column(db.Enum(Players))
    score = db.Column(db.Decimal(2,1))
    white_captures = db.Column(db.Integer)
    black_captures = db.Column(db.Integer)
    application = db.Column(db.String(40))
    application_version = db.Column(db.String(20))
    event = db.Column(db.String(40))
    name = db.Column(db.String(40))
    description = db.Column(db.String(200))
    round = db.Column(db.Integer())
    
    # foreign keys
    # game_room
    # time_settings
    # player_black
    # player_white

    def __init__(self):
        pass