from flask import Blueprint, request, jsonify, session
from database import db
from models.User import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['POST'])
def auth_signup():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        user = User.query.filter_by(username=data.get('username')).first()
        if not user:
            try:
                user = User(
                    username = data['username'],
                    email = data['email'],
                    password = data['password'],
                )
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token(user.id)
                response = {
                    'status': 'success',
                    'message': 'Succesfully registered.',
                    'token': auth_token.decode()
                }
                return jsonify(response), 201
            except Exception as e:
                print(e.__dict__)
                response = {
                    'status': 'fail',
                    'message': 'There was an error. Please try again.'
                }
                return jsonify(response), 401
        else: # username is taken
            response = {
                'status': 'fail',
                'message': 'User already exists. Please login.'
            }
    else: # email is taken
        response = {
            'status': 'fail',
            'message': 'User already exists. Please login.'
            }
        return jsonify(response), 202

@auth.route('/login', methods=['POST'])
def auth_login():
    # get the post data
    data = request.get_json()
    try:
        # fetch the user data
        print('getting here')
        print(data)
        user = User.query.filter_by(email=data['email']).first()
        print(user.username)
        auth_token = user.encode_auth_token(user.id)
        print(auth_token)
        if auth_token:
            response = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'token': auth_token.decode()
            }
            return jsonify(response), 200
    except Exception as e:
        print(e)
        response = {
            'status': 'fail',
            'message': 'Try again'
        }
        return jsonify(response), 500