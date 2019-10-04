from app import db, ma
import enum

class Languages(enum.Enum):
    EN: "English"

class GameRoom(db.Model):
    __tablename__ = "game_rooms"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    private = db.Column(db.Boolean(), nullable=False, default=False)
    language = db.Column(db.Enum(Languages), nullable=False)

    def __init__(self):
        pass