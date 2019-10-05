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
    'config.DevelopmentConfig'
)

app.config.from_object(app_settings)

# init bcrypt
bcrypt = Bcrypt(app)

# init database
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)

# init all db models
import models

migrate = Migrate(app, db)


# dev server
DEBUG = True
PORT = 8000

# Routes

@app.route('/')
def hello_world():
    return 'Hello World'

# Blue prints
from api.api import api
from auth.auth import auth

app.register_blueprint(api)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)