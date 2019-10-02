from ..app import db, ma
import enum

class Languages(enum.Enum):
    EN: "English"

class GameRoom(db.Model):
        __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(40))
    description = db.Column(db.String(200))
    private = db.Column(db.Boolean())
    language = db.Column(db.Enum(Languages))

    def __init__(self):
        pass