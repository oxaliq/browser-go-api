from flask import Blueprint

user = Blueprint('users', __name__)

@user.route('/<int:user_id>')
def func():
    pass

@user.route('/<str:user_username>')
def func():
    pass