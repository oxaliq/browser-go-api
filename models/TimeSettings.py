from ..app import db, ma
import enum

class TimeTypes(enum.Enum):
    BYOYOMI = "Counting by time period"
    ABSOLUTE = "One period to use time"
    HOURGLASS = "Absolute time for both players"
    NONE = "Untimed"

class TimeSettings(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    main_time = db.Column(db.Enum(Time))
    time_period = db.Column(db.Integer) # number of periods
    period_length = db.Column(db.Integer) # seconds
    overtime = db.Column(db.Enum())
    overtime_period = db.Column(db.Integer) # number of overtime periods
    overtime_length = db.Column(db.Integer) # seconds

    # foreing key
    game = db.Column(db.Integer, db.ForeignKey("game.id"))

    def __init__(self):
        pass