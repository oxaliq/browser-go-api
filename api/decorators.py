from flask import Blueprint, request, jsonify, session, abort
import os
import jwt

def jwt_required():
    def decorator(func):
        def authorized(*args, **kwargs):
            print(request.headers)
            auth_header = request.headers.get('Authorization') or None
            if auth_header:
                auth_token = auth_header.split(" ")[1]
                print(auth_token)
                if jwt.decode(auth_token, os.environ.get('SECRET_KEY')):
                    return func(*args, **kwargs)
                else:
                    abort(401)
            else:
                abort(401)
        return authorized
    return decorator