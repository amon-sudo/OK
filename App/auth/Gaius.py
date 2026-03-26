from flask import Flask
from models.Caeser import louis_bp

app = Flask(__name__)


app.register_blueprint(louis_bp)

if __name__ == "__main__":
    with app.app_context():
        
     app.run(debug=True)