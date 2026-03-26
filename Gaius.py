from flask import Flask
from Caeser import louis_bp

app = Flask(__name__)


app.register_blueprint(louis_bp)

if __name__ == "__main__":
    app.run(debug=True)