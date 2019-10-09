from flask import Blueprint, request, jsonify, session
import os
import jwt

def jwt_required():
    def decorator(func):
        def authorized(*args, **kwargs):
            auth_header = request.headers.get('Authorization') or None
            print(User.decode_auth_token(auth_header.split(" ")[1]))
            if auth_header:
                auth_token = auth_header.split(" ")[1]
                if jwt.decode(auth_token, os.environ.get('SECRET_KEY')):
                    return func(*args, **kwargs)
                else:
                    abort(401)
            else:
                abort(401)
        return authorized
    return decorator