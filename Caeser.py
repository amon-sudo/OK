
from Rubicon import User, storage, in_logged
from flask import Flask, request, redirect, jsonify, Blueprint
louis_bp = Blueprint("XIV", __name__)
@louis_bp.route("/register", methods = ["POST"])
def register():
    ab = request.get_json()
    default_role = "user"
    user = User(
        ab["fname"],
        ab["sname"],
        ab["username"],
        ab["email"],
        ab["password"],
        default_role
    )
    storage.append(user.to_dict())
    return jsonify({"msg": "Welcome!!",
                    "whoIsYou": default_role
                    })

def accessibility(user):
    if user["whoIsYou"] =="admin":
        return "You have full access"
    else:
        return "You are a user"

@louis_bp.route("/login", methods=["POST"])
def login():
    ab = request.get_json()
    
    user = User.find(ab["email"], ab["password"])
    if not user:
        return jsonify({"error": "register beforre you log in"})
    if user["email"] not in in_logged:
        in_logged.append(user["email"])
    allowed = accessibility(user)
    return jsonify({
            "status": "Logged in succesfuly",
            "whoIsYou": user['whoIsYou'],
            "allowed" : allowed
            
     })
@louis_bp.route("/logout")
def logout():
    pompey = request.get_json()
    email = pompey.get("email")
    if email in in_logged:
        in_logged.remove(email)
        return jsonify({"msg":"Logged out succesfully"})
    else:
        return jsonify({"msg": "logih so you can logout"})