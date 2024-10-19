from .database import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    main = db.Column(db.String(50))
    temp = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    dt = db.Column(db.Integer)

class DailySummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    date = db.Column(db.String(10))
    avg_temp = db.Column(db.Float)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    dominant_condition = db.Column(db.String(50))

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    temp = db.Column(db.Float)
    timestamp = db.Column(db.String(19))
    message = db.Column(db.String(200))
