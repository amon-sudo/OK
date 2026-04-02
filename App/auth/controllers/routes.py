from flask import Blueprint, request, jsonify, session
from auth.models import db, User, Role
from utili.middleware import who_allowed

amon_bp = Blueprint("auth", __name__, url_prefix="/auth")


print("KK")
@amon_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    fname = data.get("fname")
    sname = data.get("sname")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check missing fields
    if not all([fname, sname, username, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    # Check if user exists
    existing = User.query.filter(
        (User.email == email) | (User.username == username)
    ).first()

    if existing:
        return jsonify({"error": "User already exists"}), 409
    role = Role.query.filter_by(name = "user").first()
    if not role:
        return jsonify({"msg": "no role"})
    new_user = User(
        fname=fname,
        sname=sname,
        username=username,
        email=email,
        role = role
    )
    new_user.set_damn_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

    return jsonify({"message": "User registered successfully"}), 201




def create_admin():
    admin_role = Role.query.filter_by(name="admin").first()

    if not admin_role:
        print("Admin role not found!")
        return

    existing = User.query.filter_by(email="hannibal@g.com").first()
    if existing:
        return
    if existing:
        print("we already have admin")
    admin = User(
        fname="jj",
        sname="yy",
        username="Hannibal",
        email="hannibal@g.com",
        role=admin_role
    )
    admin.set_damn_password("0987")

    db.session.add(admin)
    db.session.commit()





@amon_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "something is wrong"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing credentials"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_damn_password(password):
        session["user_id"] = user.id
        session["role"] = user.role.name
        return jsonify({
            "message": "Login successful",
            "msg": user.role.name
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401


@amon_bp.route("/users", methods=["GET"])
@who_allowed("admin")
def users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "role": u.role.name,
            "email": u.email
        }
        for u in users
    ])

@amon_bp.route("/promote", methods=["POST"])
@who_allowed("admin")
def assign_role():
    data = request.get_json(silent=True)
    if not data:
            return jsonify({"error": "somethings wrong"}), 400
    email = data.get("email")
    role_name = data.get("role")
    if not email or not role_name:
        return jsonify({"error": "user is recquired and role required"}), 400

    # kucheck user
    user = user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    # kuangalia role
    role = Role.query.filter_by(name=role_name).first()
    print("ROLE FOUND:", role)
    if not role:
        return jsonify({"error": "Role not found"}), 404
        
    # kubadilisha role
    user.role = role

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"error": " error occured somewhwere"}), 500

    return jsonify({
        "message": "updated successfully",
        "user": user.username,
        "new_role": role.name
    }), 200





@amon_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200