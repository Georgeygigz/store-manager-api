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
            "password": "maR#@Y_123",
            "role": "user"
        }
        self.users1 = {
            "user_id": 2,
            "username": 'james',
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
            "role": "user"
        }

    '''Test test create an user account'''

    def test_user_create_account(self):
        response = self.app.post(
            '/api/v1/auth/register',
            data=json.dumps(self.users),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(
            response.json, {'message': 'Account created successfuly'})
        self.assertEqual(response.status_code, 201)

    '''Test for invalid email'''

    def test_invalid_email(self):
        response = self.app.post(
            'api/v1/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "marygmail.com",
                 "password": "maR#@Y_123",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(response.json, {'message': 'invalid Email'})
        self.assertEqual(response.status_code, 401)

    '''Test for invalid password'''

    def test_invalid_password(self):
        response = self.app.post(
            'api/v1/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "mary@gmail.com",
                 "password": "maR#@",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'})
        self.assertEqual(response.json, {'message': 'invalid password'})
        self.assertEqual(response.status_code, 401)
    
    '''Test Login'''
    def test_user_login(self):
        response=self.app.post('/api/v1/auth/login', data=json.dumps({
            'email' : 'mary@gmail.com',
            'password' : 'maR#@Y_123'
            }))
        result = json.loads(response.data.decode('utf-8'))        
        self.assertEqual(response.status_code, 200,result['message'])

    def tearDown(self):
        pass
