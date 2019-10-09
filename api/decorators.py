from flask import Blueprint, request, jsonify, session

def jwt_required():
    def decorator(func):
        def authorized(*args, **kwargs):
            auth_header = request.headers.get('Authorization') or None
            if auth_header:
                # check secret on auth header
                return func(*args, **kwargs)
            else:
                abort(401)
        return authorized
    return decorator