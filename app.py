import os

from flask import Flask

# ! SQLAlchemy > Marshmallow - these must be imported in this order
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate

from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# dev database
DATABASE = 'postgresql://localhost/browser-go'

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#init bcrypt
bcrypt = Bcrypt(app)

# init database
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)

# init all db models
from .models.User import User
from .models.GameRoom import GameRoom
from .models.TimeSettings import TimeSettings
from .models.Game import Game
from .models.Move import Move
from .models.Message import Message

migrate = Migrate(app, db)


# dev server
DEBUG = True
PORT = 8000

# Routes

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)