from scoreboard import db


class Team (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    points = db.Column(db.String(150), nullable=False, default='')  # just put a JSONified dict in here
