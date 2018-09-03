from scoreboard import db


class Team (db.Model):
    """
    points: Just put a JSONified dict in here containing exercise number : points scored pairs
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    points = db.Column(db.String(150), nullable=False, default='')
