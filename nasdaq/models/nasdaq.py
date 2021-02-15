from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MostActive(db.Model):
    symbol = db.Column(db.Unicode(5), primary_key=True)
    name = db.Column(db.Unicode(128))
    last = db.Column(db.Float, default=0.0)
    change = db.Column(db.Float, default=0.0)
    volume = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.now(), primary_key=True)

    def __init__(self, symbol, name, last, change, volume):
        self.symbol = symbol
        self.name = name
        self.last = last
        self.change = change
        self. volume = volume

    def __repr__(self):
        return '<MostActive %r>' % self.name
