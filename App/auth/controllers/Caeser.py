
from Julius.App.auth.models.Rubicon import User, storage, in_logged
from flask import Flask, request, redirect, jsonify, Blueprint
louis_bp = Blueprint("XIV", __name__)
@louis_bp.route("/register", methods=["POST"])
def register():
    try:
        ab = request.get_json(force=True)
        if not ab:
            return jsonify({"err": "Empty request body"}), 400
        for f in ["fname", "sname", "username", "email", "password"]:
            if f not in ab:
                return jsonify({"error": f"Missing field: {f}"}), 400
            
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
        b2 = user.fname

        return jsonify({"msg": f"Welcome!!  {b2}",
                       "whoIsYou": default_role 
                        })

    except Exception:
        return jsonify({"err": "Invalid JSON"}), 400

    
def accessibility(user):
    if user["whoIsYou"] =="Admin":
        return "You have full access"
    if user["whoIsYou"] == "Manager":
        return "Welcome Manager"
    if user["whoIsYou"]  == "Sales":
        return "You need to kill the market"
    if user["whoIsYou"] == "employee":
        return "Work hard my friend, you are an employ"
    else:
        return "You are a user"

@louis_bp.route("/login", methods=["POST"])
def login():
    try:
        
        ab = request.get_json()
        if not ab:
            return jsonify({"err":"Nothing here"})
        
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
    except Exception:
        return({"err": "somethings wrong"})
@louis_bp.route("/logout", methods = ["POST"])
def logout():
    try:
        pompey = request.get_json()
        email = pompey.get("email")
        if email in in_logged:
            in_logged.remove(email)
            return jsonify({"msg":"Logged out succesfully"})
        else:
            return jsonify({"msg": "logih so you can logout"})
    except Exception:
        return jsonify({"err" : "something went bad"})    
    
@louis_bp.route("/users", methods=["GET"])
def users():
    return jsonify({
        "users": storage
    }), 200
    
@louis_bp.route("/alreadyLogged")
def alreadyLogged():
    return jsonify({
        "users" : in_logged
    }), 200
    
@louis_bp.route("/promote", methods=["POST"])
def promote_user():
    try:
        bp = request.get_json()
        
        admin_email = bp.get("admin_email")
        promote_email = bp.get("promote_email")
        
        if admin_email not in in_logged:
            return jsonify({"error": "Login required"}), 401
        
        admin_user = User.find_by_email(admin_email)
        if not admin_user or admin_user["whoIsYou"] != "Admin":
            return jsonify({"error": "Only admins can promote users"}), 403
        
        user_to_promote = User.find_by_email(promote_email)
        if not user_to_promote:
            return jsonify({"err": "User not found"}), 404
        user_to_promote["whoIsYou"] = "Admin"
        
        return jsonify({"msg": "Happy New Admin"})
    except Exception:
        return ({"err" : "somethin went bad"})
    
@louis_bp.route("/all", methods=["GET"])
def all():
    return jsonify(storage)