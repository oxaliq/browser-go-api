from app import db, ma
#   TODO    User >---< GameRoom
import enum

game_rooms_users = db.Table('game_rooms_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('game_rooms_id', db.Integer, db.ForeignKey('game_rooms.id'), primary_key=True)
)

class Languages(enum.Enum):
    EN = "English"

class GameRoom(db.Model):
    __tablename__ = "game_rooms"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    private = db.Column(db.Boolean(), nullable=False, default=False)
    language = db.Column(db.Enum(Languages), nullable=False)

    # ! Foreign Keys
    users = db.relationship(
        'User', 
        secondary=game_rooms_users, 
        lazy='subquery',
        backref=db.backref('game_rooms', lazy=True)
        )

    def __init__(self, name, description, private=False, language=Languages.EN):
        self.name = name
        self.description = description
        self.private = private
        self.language = language
