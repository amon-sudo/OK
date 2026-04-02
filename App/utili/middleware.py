from functools import wraps
from flask import jsonify, session
from auth.models import User


def who_allowed(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            user_id = session.get("user_id")
            role = session.get("role")

            if not user_id or not role:
                return jsonify({"error": "Unauthorized"}), 401

            
            user = User.query.get(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            if user.role.name not in allowed_roles:
                return jsonify({
                    "error": "Forbidden",
                    "your_role": user.role.name,
                    "allowed_roles": allowed_roles
                }), 403

            return f(*args, **kwargs)

        return wrapper
    return decorator