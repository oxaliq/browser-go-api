from app import db, ma
from marshmallow import fields
import enum
#   TODO    User >---< GameRoom

# ! Game Rooms >-< Users join table
game_rooms_users = db.Table('game_rooms_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('game_rooms_id', db.Integer, db.ForeignKey('game_rooms.id'), primary_key=True)
)

class GameRoom(db.Model):
    __tablename__ = "game_rooms"
    __table_args__ = {'extend_existing': True}
    
    class Languages(enum.Enum):
        EN = "English"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    private = db.Column(db.Boolean(), nullable=False, default=False)
    language = db.Column(db.Enum(Languages), nullable=False, default=Languages.EN)

    def __init__(self, name, description, private=False, language=Languages.EN):
        self.name = name
        self.description = description
        self.private = private
        self.language = language

class RoomSchema(ma.ModelSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    private = fields.Bool()
    language = fields.Str()
        

room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)