from scoreboard import db


class Exercise (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.SmallInteger, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(1000), nullable=False, default='')
    visible = db.Column(db.Boolean, default=False)

