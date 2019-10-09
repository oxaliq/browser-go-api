from app import db, ma
#   TODO    User >---< GameRoom

# ! Game Room >-< Users join table
game_rooms_users = db.Table('game_rooms_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('game_rooms_id', db.Integer, db.ForeignKey('game_rooms.id'), primary_key=True)
)

class RoomLanguages(db.Model):
    __tablename__ = "room_languages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    iso = db.Column(db.String(2), nullable=False)


class GameRoom(db.Model):
    __tablename__ = "game_rooms"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    private = db.Column(db.Boolean(), nullable=False, default=False)

    # ! Foreign Keys
    users = db.relationship(
        'User', 
        secondary=game_rooms_users, 
        lazy='subquery',
        backref=db.backref('game_rooms', lazy=True)
        )
    
    language = db.Column(db.Integer, db.ForeignKey("room_languages.id"), nullable=False)
    

    def __init__(self, name, description, private=False, language=1):
        self.name = name
        self.description = description
        self.private = private
        self.language = language
