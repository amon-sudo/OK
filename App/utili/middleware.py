from functools import wraps
from flask import jsonify, request, session


def who_allowed(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            role = session.get("role")

            if not role:
                return jsonify({"error": "Unauthorized"}), 401

            if role not in allowed_roles:
                return jsonify({"error": "Forbidden"}), 403

            return f(*args, **kwargs)

        return wrapper
    return decorator