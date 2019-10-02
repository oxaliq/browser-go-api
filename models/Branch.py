from ..app import db, ma

class Branch(db.Model):
        __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)