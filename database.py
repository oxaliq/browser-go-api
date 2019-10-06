
# ! SQLAlchemy > Marshmallow - these must be imported in this order
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
    
# init bcrypt
def bcrypt(app):
    Bcrypt(app)

# init database
db = SQLAlchemy()

# init marshmallow
ma = Marshmallow()
