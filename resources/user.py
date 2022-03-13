from flask_restful import Resource, reqparse
from models.user import UserModel
from security import require_apikey


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('gender', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('ip_address', type=str)
    parser.add_argument('country_code', type=str)

    @classmethod
    @require_apikey
    def get(cls, user_id):
        user = UserModel.find_by_user_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    @require_apikey
    def delete(cls, user_id):
        user = UserModel.find_by_user_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        user.delete_from_db()
        return {'message': 'User deleted'}

    @require_apikey
    def put(self, user_id):
        data = User.parser.parse_args()

        user = UserModel.find_by_user_id(user_id)

        if user is None:
            user = UserModel(user_id, **data)
        else:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.gender = data['gender']
            user.email = data['email']
            user.ip_address = data['ip_address']
            user.country_code = data['country_code']

        user.save_to_db()

        return user.json()


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('gender', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('ip_address', type=str)
    parser.add_argument('country_code', type=str)

    @require_apikey
    def post(self):
        data = UserRegister.parser.parse_args()

        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {'message': "An error occurred inserting the item"}, 500

        return {'message': "User added"}, 201
