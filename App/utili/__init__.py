from functools import wraps

def rolee(*all_roles):
    def decorator(f):
        @wraps(f)
        def epper(*args, **kwargs):
            role = session.get("role")
            
            if not role:
                return jsonify({"err":"unauthorized"}), 401
            if role not in all_roles:
                return jsonify({"error":"not a member"}), 403
        
            return f(*args, **kwargs)
        return epper
    return decorator