from flask import Blueprint, request, jsonify, session
from ..models.User import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@api.route('/signup', methods=['POST'])
def auth_signup():
    response = {"message": "signup post"}
    return jsonify(response)

@api.route('/login', methods=['POST'])
def auth_login():
    response = {"message": "login post"}
    return jsonify(response)