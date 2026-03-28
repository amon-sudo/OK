from flask import Flask
from auth.controllers.routes import amon_bp


app = Flask(__name__)
app.config['SECRETE_KEY'] = 'amon-admiral-zheng-he'
app.config['DATABASE_URI'] = 'sqlite:///app.db'


app.register_blueprint(amon_bp)


if __name__ == "__main__":
    with app.app_context():
        
     app.run(debug=True)