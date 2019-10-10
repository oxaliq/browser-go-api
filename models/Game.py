from app import db, ma
from marshmallow import fields
import enum
from models.User import user_schema


class Game(db.Model):
    __tablename__ = "games"
    __table_args__ = {'extend_existing': True}
    
    class Players(enum.Enum):
        BLACK = "The player taking black stones"
        WHITE = "The player taking white stones"
        VOID = "The game was a draw or voided"

    class WinType(enum.Enum):
        DRAW = "The game is a draw"
        RESIGN = "The game ended in resignation"
        SCORE = "The game ended by counting points"
        TIME = "The game ended in loss by time out"
        VOID = "The game was suspended"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime())
    komi = db.Column(db.Numeric(2,1), nullable=False)
    handicap = db.Column(db.Integer, nullable=False)
    board_size = db.Column(db.Integer, nullable=False)
    win_type = db.Column(db.Enum(WinType))
    winner = db.Column(db.Enum(Players))
    score = db.Column(db.Numeric(2,1))
    white_captures = db.Column(db.Integer)
    black_captures = db.Column(db.Integer)
    application = db.Column(db.String(40))
    application_version = db.Column(db.String(20))
    event = db.Column(db.String(40))
    name = db.Column(db.String(40))
    description = db.Column(db.String(200))
    round = db.Column(db.Integer)
    
    # foreign keys
    game_room = db.Column(db.Integer, db.ForeignKey("game_rooms.id"))
    time_settings = db.Column(db.Integer, db.ForeignKey("time_settings.id"))
    player_black = db.Column(db.Integer, db.ForeignKey("users.id"))
    player_white = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, name, description, board_size, game_room, player_white, komi=0.5, handicap=0, time_settings=1):
        self.name = name
        self.description = description
        self.board_size = board_size
        self.game_room = game_room
        self.player_white = player_white
        self.komi = komi
        self.handicap = handicap
        self.time_settings = time_settings
        print('did it')

class GameSchema(ma.ModelSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    boardSize = fields.Int()
    player = fields.Nested(user_schema)

game_schema = GameSchema()
games_schema = GameSchema(many=True)