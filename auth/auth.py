from flask import Blueprint, request, jsonify, session
from models import User
print(User)
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['POST'])
def auth_signup():
    response = {"message": "signup post"}
    return jsonify(response)

@auth.route('/login', methods=['POST'])
def auth_login():
    response = {"message": "login post"}
    return jsonify(response)