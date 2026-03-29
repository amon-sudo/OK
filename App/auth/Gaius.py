from flask import Flask
from auth.controllers.routes import amon_bp
from auth.models import  User, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'amon-admiral-zheng-he'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)

app.register_blueprint(amon_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)