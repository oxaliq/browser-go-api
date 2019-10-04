from app import db, ma
import enum

class Players(enum.Enum):
    BLACK = "The player taking black stones"
    WHITE = "The player taking white stones"

class Message(db.Model):
    __tablename__ = "messages"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    # foreign key
    move = db.Column(db.Integer, db.ForeignKey("moves.id"), nullable=False)

    def __init__(self):
        pass