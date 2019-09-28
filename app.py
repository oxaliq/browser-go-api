import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# dev database
DATABASE = 'postgresql://localhost/browser-go'

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)

# dev server
DEBUG = True
PORT = 8000

# Routes

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)