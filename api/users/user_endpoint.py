from models.User import User, user_schema, users_schema
from flask import request, jsonify, Response, json

class UserEndpoint(object):
    def users():
        users = User.query.all()
        response = users_schema.dumps(users)
        return response
    def user():

        auth_header = request.headers.get('Authorization') or None
        auth_token = auth_header.split(" ")[1]
        user = User.decode_auth_token(auth_token) or None
        response = json.dumps(user)
        return response