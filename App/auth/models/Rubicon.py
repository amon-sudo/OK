from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    create_at = db.Column(db.DateTime, default=db.func.current_timestampl())
    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(), nullable = False)
    fname = db.Column(db.String(50),  nullable = False)
    sname = db.Column(db.String(50),  nullable = False)
    username = db.Column(db.String(60), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password_damn_hashed = db.Column(db. String(120), nullable = False)
    
    def __init__(self, fname, sname, username, email):
        self.fname = fname
        self.sname = sname
        self.username = username
        self.email = email 
    def set_damn_password(self, password):
        self.password_damn_hashed = generate_password_hash(password)
        
        
    def checking_damn_password(self, password):
        return check_password_hash(self.password_damn_hashed, password)
