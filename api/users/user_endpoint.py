from models.User import User, user_schema

class UserEndpoint(object):
    def users():
        user = User.query.first()
        response = user_schema.dumps(user)
        return response
