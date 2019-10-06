
# ! SQLAlchemy > Marshmallow - these must be imported in this order
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
    
# init database
db = SQLAlchemy()

# init marshmallow
ma = Marshmallow()
