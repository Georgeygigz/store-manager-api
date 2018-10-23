# app/api/v1/views/auth_views.py
'''This is where all authentication Endpoints will be captured'''
import re
import jwt
from flask import request,jsonify, make_response
import datetime
from functools import wraps
from passlib.hash import sha256_crypt

from flask_restful import Resource,reqparse

# import class products
from app.api.v1.models.store_model import Users
from app.api.v1.utils.utils import Validate

users =Users().get_all_users()


'''Create a new account'''

'''create a token decorator function that generates authentication token'''
def login_required(func):
    @wraps(func)
    def decorator_func(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        if not token:
            return make_response(jsonify({"message":"Please Login inorder for you to continue"}))
        try:
            data=jwt.decode(token,"secret")
            current_user=[user for user in users if user['user_id']==data['user_id']]
        except:
            return make_response(jsonify({"message":"Invalid token"}),401)
        
        return func(current_user,*args, **kwargs)
    return decorator_func

class CreateAccount(Resource):
    
    def post(self):
        '''
        Create an account for new user
        '''
        data = request.get_json(force=True)
        Validate().validate_empty_users_inputs(data)
        user_id = len(users)+1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]
        single_user=[user for user in users if user['email']==request.json['email']]
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', request.json['email']):
            return make_response(jsonify({"message": "invalid Email"}), 401)

        if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])', request.json['password']):
            return make_response(jsonify({"message": "invalid password"}), 401)

        new_user_detail = {"user_id": user_id,
                           "username": username,
                           "email": email,
                           "password": sha256_crypt.encrypt(password),
                           "role": role}
        
        if not single_user :
            new_user=Users()
            new_user.insert_new_user(**new_user_detail)
            return make_response(jsonify({"message": "Account created successfuly"}), 201)

        return make_response(jsonify({"Message": " {} Aready Exist".format(request.json['email'])}), 409)  # conflict

class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        email=data['email']
        get_password=data['password']
        cur_user=[c_user for c_user in users if c_user['email']==email]

        if  len(cur_user) > 0:		
            password =cur_user[0]['password']
            if sha256_crypt.verify(get_password, password):
                exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=20)
                token = jwt.encode({'user_id': cur_user[0]['user_id'],'exp': exp_time},"secret")
                result={"message":"Login succesful","token":token.decode('utf-8')}
                
            else:
                return make_response(jsonify({"message":"Invalid Password"}))
        else:
            return make_response(jsonify({"message":"Invalid Email. If have not account, register"}))

        return result,200