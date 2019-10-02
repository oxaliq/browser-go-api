from ..app import db, ma
import enum

class Players(enum.Enum):
    BLACK = "The player taking black stones"
    WHITE = "The player taking white stones"

class Message(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    content = db.Column(db.String(200))

    # foreing key
    game = db.Column(db.Integer, db.ForeignKey("move.id"))

    def __init__(self):
        pass