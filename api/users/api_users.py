from models.User import User, user_schema, users_schema
from flask import Blueprint, request, json, session, jsonify
from ..decorators import jwt_required

api_users = Blueprint('api_users', __name__, url_prefix='/api')

@api_users.route('/users/', methods=['GET'])
def api_get_users():
    print('called one')
    users = User.query.all()
    response = users_schema.dumps(users)
    return jsonify(response), 200


@api_users.route('/users/account', methods=['GET'])
@jwt_required()
def api_get_user():
    print('called')
    auth_header = request.headers.get('Authorization') or None
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        user = User.decode_auth_token(auth_token) or None
        response = json.dumps(user)
    else: 
        response = {
            'status': 'failed',
            'message': 'Please Log In'}
    return jsonify(response)
