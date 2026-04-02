from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from . import db



class Role:
    id = db.Column(db.Integer, primary_key =  True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    
    
    def __repr__(self):
        return f"Role {self.name}"

class User(db.Model):
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(50),  nullable = False)
    sname = db.Column(db.String(50),  nullable = False)
    username = db.Column(db.String(60), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    role_id = db.Column(db.String(200), db.models.ForeignKey("role_id"))
    role = db.relationship("role")
    password_damn_hashed = db.Column(db.String(120), nullable = False)
    
    def __init__(self, fname, sname, username, email, role="user"):
        self.fname = fname
        self.sname = sname
        self.username = username
        self.email = email 
        self.role = role
    def set_damn_password(self, password):
        self.password_damn_hashed = generate_password_hash(password)
        
        
    def check_damn_password(self, password):
        return check_password_hash(self.password_damn_hashed, password)
