from flask import Flask
from flask_sqlalchemy import SQLalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)

class Message(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(30))
    to = db.Column(db.String(30))
    content = db.Column(db.String(100))
    status = db.Column(db.String(30))

class Room(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
    room_type = db.Column(db.String(20))
    is_booked = db.Column(db.Boolean)

class Flight(db.Model):
    number = db.Column(db.String(6), primary_key=True)
    airport_from = db.Column(db.String(3))
    airport_to = db.Column(db.String(3))
    aircraft = db.Column(db.Boolean)

class ProgammingLanguage(db.Model):
    name = db.Column(db.String(20))
    invented_at = db.Column(db.Integer)
    is_nice = db.Column(db.Boolean)
    is_modern = db.Column(db.Boolean)
    is_popular = db.Column(db.Boolean)
