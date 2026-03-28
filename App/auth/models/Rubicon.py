from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.integer, primary_key = True)
    role = db.Column(db.String(), nullable = False)
    fname = db.Column(db.String(50), unique = True, nullable = False)
    sname = db.Column(db.Stringt(50), unique = True, nullable = False)
    username = db.Column(db.String(60), unique = True, nullable = False)
    email = db.Column(db.String(100), uniques = True, nullable = False)
    password_damn_hashed = db. Column(db. String(20), nullable = False)
    
    
    def set_damn_password(self, password):
        self.password_hashed = generate_password_hash(password)
        
        
    def checking_damn_password(self, password):
        return check_password_hash(self.password_damn_hashed, password)
