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

# config database
app_settings = os.getenv(    
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

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

@app.route('/api')


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)