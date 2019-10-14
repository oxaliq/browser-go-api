from app import db, ma
from marshmallow import fields, Schema, pre_dump
import enum
from models.User import UserSchema, user_schema, User

# ! Games >-< Users join table
games_users = db.Table('games_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('game_rooms_id', db.Integer, db.ForeignKey('games.id'), primary_key=True)
)

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

    class TimeTypes(enum.Enum):
        BYOYOMI = "Counting by time period"
        ABSOLUTE = "One period to use time"
        HOURGLASS = "Absolute time for both players"
        NONE = "Untimed"

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
    main_time = db.Column(db.Enum(TimeTypes), nullable=False)
    time_period = db.Column(db.Integer) # number of periods
    period_length = db.Column(db.Integer) # seconds
    overtime = db.Column(db.Enum(TimeTypes), nullable=False)
    overtime_period = db.Column(db.Integer) # number of overtime periods
    overtime_length = db.Column(db.Integer) # seconds
    
    # foreign keys
    game_room = db.Column(db.ForeignKey("game_rooms.id"))
    player_black = db.Column(db.ForeignKey("users.id"))
    player_white = db.Column(db.ForeignKey("users.id"))

    def __init__(
        self, name, description, board_size, game_room, player_white, 
        komi=0.5, handicap=0, main_time=TimeTypes.NONE, overtime=TimeTypes.NONE
    ):
        self.name = name
        self.description = description
        self.board_size = board_size
        self.game_room = game_room
        self.player_white = player_white
        self.komi = komi
        self.handicap = handicap
        self.main_time = main_time
        self.overtime = overtime

class GameSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    board_size = fields.Int()
    game_room = fields.Int()
    # TODO change players to fields.Nested(UserSchema) 
    # TODO when you figure out why it's not working
    player_black = fields.Int()
    player_white = fields.Int()

        
game_schema = GameSchema()
games_schema = GameSchema(many=True)