from scoreboard import db


class Exercise (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.SmallInteger, nullable=False)
    text = db.Column(db.String(1000), nullable=False)

