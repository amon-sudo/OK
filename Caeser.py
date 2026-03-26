
from Rubicon import User, storage, in_logged
from flask import Flask, request, redirect, jsonify, Blueprint
louis_bp = Blueprint("XIV", __name__)
@louis_bp.route("/register", methods = ["POST"])
def register():
    ab = request.get_json()
    default_role = "user"
    user = User(
        ab["username"],
        ab["email"],
        ab["password"],
        default_role
    )
    storage.append(user.to_dict())
    return jsonify({"msg": "Welcome!!","whoIsYou": default_role })

def accessibility(user):
    if user["whoIsYou"] =="Admin":
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
@louis_bp.route("/logout", methods = ["POST"])
def logout():
    pompey = request.get_json()
    email = pompey.get("email")
    if email in in_logged:
        in_logged.remove(email)
        return jsonify({"msg":"Logged out succesfully"})
    else:
        return jsonify({"msg": "logih so you can logout"})
    
    
@louis_bp.route("/users", methods=["GET"])
def users():
    return jsonify({
        "users": storage
    })
    
@louis_bp.route("/alreadyLogged")
def alreadyLogged():
    return jsonify({
        "users" : in_logged
    })
    
@louis_bp.route("/promote", methods=["POST"])
def promote_user():
    data = request.get_json()
    
    admin_email = data.get("admin_email")
    promote_email = data.get("promote_email")
    
    if admin_email not in in_logged:
        return jsonify({"error": "Login required"}), 401
    
    admin_user = User.find_by_email(admin_email)
    if not admin_user or admin_user["whoIsYou"] != "Admin":
        return jsonify({"error": "Only admins can promote users"}), 403
    
    user_to_promote = User.find_by_email(promote_email)
    if not user_to_promote:
        return jsonify({"err": "User not found"}), 404
    user_to_promote["whoIsYou"] = "admin"
    
    return jsonify({"msg": "Happy New Admin"})