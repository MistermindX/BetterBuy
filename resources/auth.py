from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password


class Register(Resource):
    def post(self):
        data = request.get_json()
        params = {
            "name": data['name'],
            "address": data['address'],
            "email": data['email'],
            "password_digest": gen_password(data['password'])
        }
        user = User(**params)
        user.create()
        return user.json(), 201


class Login(Resource):
    def post(self):
        pass

    def get(self):
        pass
