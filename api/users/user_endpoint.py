from models.User import User, user_schema, users_schema

class UserEndpoint(object):
    def users():
        user = User.query.all()
        response = users_schema.dumps(user)
        return response
