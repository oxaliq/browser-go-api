from flask import Blueprint, request, jsonify, session
from .users.user_endpoint import UserEndpoint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/home', methods=['GET'])
def api_home():
    response = {"message": "home page"}
    return jsonify(response)

@api.route('/users')
def api_users():
    return jsonify(UserEndpoint.users())
