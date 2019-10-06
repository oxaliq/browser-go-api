from flask import Blueprint, request, jsonify, session

from database import db
from models.User import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['POST'])
def auth_signup():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        try:
            print('getting here 1')
            user = User(
                email = data['email'],
                password = data['password'],
            )
            print('getting here 2')
            db.session.add(user)
            print('wtf')
            db.session.commit()
            print('user')
            auth_token = user.encode_auth_token(user.id)
            print('getting here 4')
            response = {
                'status': 'success',
                'message': 'Succesfully registered.',
                'auth_token': auth_token.decode()
            }
            return jsonify(response), 201
        except Exception as e:
            print(e.__dict__)
            response = {
                'status': 'fail',
                'message': 'There was an error. Please try again.'
            }
            return jsonify(response), 401
    else: 
        response = {
            'status': 'fail',
            'message': 'User already exists. Please login.'
            }
        return jsonify(response), 202

@auth.route('/login', methods=['POST'])
def auth_login():
    response = {"message": "login post"}
    return jsonify(response)