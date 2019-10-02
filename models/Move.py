from ..app import db, ma
import enum

class Players(enum.Enum):
    BLACK = "The player taking black stones"
    WHITE = "The player taking white stones"

class Branch(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.Enum(Players))
    x_point = db.Column(db.Integer)
    y_point = db.Column(db.Integer)
    move_number = db.Column(db.Integer)

    # foreign keys
    game = db.Column(db.Integer, db.ForeignKey("game.id"))

    def __init__(self):
        pass