from database import db, ma
from marshmallow import fields, Schema
from app import bcrypt
from configuration import config
import datetime
import enum
import json
import jwt
import os


class User(db.Model):
    __tablename__ = "users"

    class Ranks(enum.Enum): # with minimal Elo rating
        D7 = "Seven Dan" # Elo 2700+
        D6 = "Six Dan"
        D5 = "Five Dan" # Elo 2500
        D4 = "Four Dan"
        D3 = "Three Dan"
        D2 = "Two Dan"
        D1 = "One Dan"
        K1 = "One Kyu" # Elo 2000
        K2 = "Two Kyu"
        K3 = "Three Kyu"
        K4 = "Four Kyu"
        K5 = "Five Kyu"
        K6 = "Six Kyu" # Elo 1500
        K7 = "Seven Kyu"
        K8 = "Eight Kyu"
        K9 = "Nine Kyu"
        K10 = "Ten Kyu"
        K11 = "Eleven Kyu" # ELo 1000
        K12 = "Twelve Kyu"
        K13 = "Thirteen Kyu"
        K14 = "Fourteen Kyu"
        K15 = "Fifteen Kyu"
        K16 = "Sixteen Kyu" # Elo 500
        K17 = "Seventeen Kyu"
        K18 = "Eighteen Kyu"
        K19 = "Nineteen Kyu"
        K20 = "Twenty Kyu"
        K21 = "Twenty-One Kyu" # Elo 0
        K22 = "Twenty-Two Kyu"
        K23 = "Twenty-Three Kyu"
        K24 = "Twenty-Four Kyu"
        K25 = "Twenty-Five Kyu"
        K26 = "Twenty-Six Kyu" # Elo -500
        K27 = "Twenty-Seven Kyu"
        K28 = "Twenty-Eight Kyu"
        K29 = "Twenty-Nine Kyu"
        K30 = "Thirty Kyu" # Elo -900
        UR = "Unknown Rank"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    rank = db.Column(db.Enum(Ranks))
    elo = db.Column(db.Integer)
    rank_certainty = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, username, email, password, rank=Ranks.UR, admin=False):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, 13
        ).decode()
        self.rank = rank
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=4),
                'iat': datetime.datetime.utcnow(),
                'user': user_schema.dumps(self)
            }
            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'))
            return payload['user']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    registered_on = fields.Date()
    rank = fields.Str()
    rank_certainty = fields.Bool()
    elo = fields.Int()
        
    class Meta:
        register=True

user_schema = UserSchema()
users_schema = UserSchema(many=True)