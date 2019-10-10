from app import db, ma
import enum


class TimeSettings(db.Model):
    __tablename__ = "time_settings"
    __table_args__ = {'extend_existing': True}

    class TimeTypes(enum.Enum):
        BYOYOMI = "Counting by time period"
        ABSOLUTE = "One period to use time"
        HOURGLASS = "Absolute time for both players"
        NONE = "Untimed"
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    main_time = db.Column(db.Enum(TimeTypes), nullable=False)
    time_period = db.Column(db.Integer) # number of periods
    period_length = db.Column(db.Integer) # seconds
    overtime = db.Column(db.Enum(TimeTypes), nullable=False)
    overtime_period = db.Column(db.Integer) # number of overtime periods
    overtime_length = db.Column(db.Integer) # seconds


    def __init__(self, main_time=TimeTypes.NONE, overtime=TimeTypes.NONE):
        self.main_time = main_time
        self.overtime = overtime