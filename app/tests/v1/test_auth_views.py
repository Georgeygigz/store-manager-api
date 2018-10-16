# app/test/v1/test_views.py

'''
Testing authentication endpoints
'''

import unittest
import json
from app import create_app


class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        '''
        Code executed before every test
        '''
        self.app = create_app().test_client()
        self.app.testing = True
        self.users = {
            "user_id": 1,
            "username": 'mary',
            "email": "mary@gmail.com",
            "password": "maR#@Y_123"
        }

    def test_user_already_exist(self):
        ''' Test for duplicate emails'''
        post_result = self.app.post(
            '/app/v1/signup',
            data=json.dumps(self.users),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(post_result.json, {'geoe@gmail.com': 'Aready Exist'})
        self.assertEqual(post_result.status_code, 409)

    '''Test test create an user account'''
    def test_user_create_account(self):
        response = self.app.post(
            '/app/v1/signup',
            data=json.dumps(self.users),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(
            response.json, {'message': 'Account created successfuly'})
        self.assertEqual(response.status_code, 201)

    '''Test for invalid email'''
    def test_invalid_email(self):
        response = self.app.post(
            'app/v1/signup',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "marygmail.com",
                 "password": "maR#@Y_123"}
            ),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(response.json, {'message': 'invalid Email'})
        self.assertEqual(response.status_code, 401)

    '''Test for invalid password'''
    def test_invalid_password(self):
        response = self.app.post(
            'app/v1/signup',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "mary@gmail.com",
                 "password": "maR#@"}
            ),
            headers={'content_type': 'application/json'})
        self.assertEqual(response.json, {'message': 'invalid password'})
        self.assertEqual(response.status_code, 401)
