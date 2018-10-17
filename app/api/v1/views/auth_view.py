# app/api/v1/views/auth_views.py
'''This is where all authentication Endpoints will be captured'''
import re
import jwt
from flask import request
from datetime import date
from flask_jwt_extended import get_raw_jwt
from functools import wraps
from passlib.hash import sha256_crypt

from flask_restful import Resource

# import class products
from app.api.v1.models.store_model import StoreManager

users = StoreManager().get_all_store_attedant()

'''Create a new account'''


class CreateAccount(Resource):
    def get(self):
        return {"Users": users}, 409  # conflict

    def post(self):
        '''
        Create an account for new user
        '''
        data = request.get_json(force=True)
        user_id = len(users)+1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', request.json['email']):
            return {"message": "invalid Email"}, 401

        if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])', request.json['password']):
            return {"message": "invalid password"}, 401

        new_user_detail = {"user_id": user_id,
                           "username": username,
                           "email": email,
                           "password": sha256_crypt.encrypt(password),
                           "role": role}

        if request.json['email'] not in [user['email'] for user in users]:
            users.append(new_user_detail)
            return {"message": "Account created successfuly"}, 201

        return {"Message": " {} Aready Exist".format(request.json['email'])}, 409  # conflict

