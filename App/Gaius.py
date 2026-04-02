from flask import Flask,jsonify, request
from auth.controllers.routes import amon_bp, create_admin
from auth.models import  User, db
from utili.Checking import role_original
app = Flask(__name__)
app.config['SECRET_KEY'] = 'amon-admiral-zheng-he'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)

app.register_blueprint(amon_bp)


@app.errorhandler(401)
def unauthorised(e):
    return jsonify({
        "error":"unauthoried"
    })
@app.errorhandler(403)
def unauth(e):
    return({
        "errer":"are you an admin?"
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Route not found"
    }), 404



@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "error": "Method not allowed",
        "message": "Check your HTTP method (GET, POST, etc)"
    }), 405

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "error": "Internal server error"
    }), 500
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        role_original()
        create_admin()
    app.run(debug=True)