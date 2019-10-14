from app import db, ma
import enum


class Move(db.Model):
    __tablename__ = "moves"
    __table_args__ = {'extend_existing': True}

    class Players(enum.Enum):
        BLACK = "The player taking black stones"
        WHITE = "The player taking white stones"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player = db.Column(db.Enum(Players))
    x_point = db.Column(db.Integer)
    y_point = db.Column(db.Integer)
    move_number = db.Column(db.Integer)
    is_pass = db.Column(db.Boolean, nullable=False, default=False)
    is_main = db.Column(db.Boolean, nullable=False, default=True)

    # foreign keys
    game = db.Column(db.ForeignKey("games.id"), nullable=False)
    preceding_move = db.Column(db.Integer, db.ForeignKey("moves.id"))


    def __init__(self, game_id, player, x_point, y_point, move_number, is_pass=True, is_main=True, preceding_move=None):
        self.game = game_id
        if player == 'black': 
            self.player = 'BLACK'
        else:
            self.player = 'WHITE'
        self.x_point = x_point
        self.y_point = y_point
        self.move_number = move_number
        self.is_pass = is_pass
        self.is_main = is_main
        self.preceding_move = preceding_move

Move.succeeding_moves = db.relationship(
    'Move',
    lazy='subquery',
    backref=db.backref('moves', lazy=True),
    remote_side=Move.id
)