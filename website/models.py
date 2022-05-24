# database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Foreign key (relate a specific note to specific user)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # UID (primary key)
    email = db.Column(db.String(150), unique=True) # Users email
    password = db.Column(db.String(150)) # Users password
    first_name = db.Column(db.String(150)) # Users first name
    notes = db.relationship('Note') # So we can access all of users notes

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generatedPassword = db.Column(db.String(10000))
    date = date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

