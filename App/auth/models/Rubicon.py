from flask import Flask, jsonify
storage = []
in_logged = []

class User:
    idd = 1
    def __init__(self,fname,sname, username, email, password, whoIsYou):
        self.id = User.idd
        User.idd +=1
        self.fname = fname
        self.sname = sname
        self.username = username
        self.email = email
        self.password = password
        self.whoIsYou = whoIsYou
        
        
    def to_dict(self):
        return {
            "id": self.id,
            "fname":self.fname,
            "sname": self.sname,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "whoIsYou" : self.whoIsYou
        }
        
    @staticmethod 
    def find(email, password):
        for u in storage:
            if u["email"] == email and u["password"] == password:
                return u
        return  jsonify({
            "msg": "seems like you are not here"
        }), 404
    
    @staticmethod
    def find_by_email(email):
        for user in storage:
            if user["email"] == email:
                return user
        return None
        
Plato = User(
    fname="prince",
    sname="Edward",
    username="thegreat",
    email="admin@1.com",
    password="4321",
    whoIsYou="Admin"
)

storage.append(Plato.to_dict())