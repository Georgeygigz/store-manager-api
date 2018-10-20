# app/tests/v1/test_storeviews.py
import unittest
import json
import jwt
from app import create_app

'''
Creating a new testing  class
'''


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.products = {"product_id": 1,
                         "product_name": "Bread",
                         "category_id": 1,
                         "stock_amount": 2000,
                         "price": 20,
                         "low_inventory_stock": 2
                         }
        self.sales = {"sale_id": 1,
                      "attedant_name": "Mary",
                      "customer_name": "James",
                      "product_name": "Bread",
                      "product_price": 20,
                      "quantity": 3,
                      "total_price": 60,
                      "date_sold": "12-3-2018"}

        self.user = {
            "user_id": 1,
            "username": 'mary',
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
            "role": "user"
        }
        self.user1={
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
        }

    def register_user(self):
        return self.app.post(
            '/api/v1/auth/register',
            data=json.dumps(self.user),
            content_type='application/json')

    def user_login(self):
        self.register_user()
        response = self.app.post('/api/v1/auth/login',
                                 data=json.dumps(self.user1))
        result = json.loads(response.data.decode('utf-8'))
        return result

    def get_user_token(self):
        '''Generate Token'''
        resp_login = self.user_login()
        token = resp_login.get("token")

        return token

    def test_config(self):
        '''Test configurations'''
        self.assertEqual(self.app.testing, True)

    '''Test get all products'''
    def test_get_all_products(self):
        access_token=self.get_user_token()
        response = self.app.get(
            '/api/v1/products',
            headers={"content_type":'application/json',"x-access-token":access_token}
        )
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200,
                         result['Available Products'])

    '''Test add new product'''

    def test_add_new_product(self):
        with self.app:
            access_token=self.get_user_token()
            response = self.app.post(
                '/api/v1/products',
                headers={"content_type":'application/json',"x-access-token":access_token},
                data=json.dumps(self.products)
            
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 201, result['New Product'])

    '''Test fetch for specific product'''

    def test_fetch_single_product(self):
        '''Test fetch for single product [GET request]'''
        with self.app:
            access_token=self.get_user_token()
            response = self.app.get(
                '/api/v1/products/1',
                headers={"content_type":'application/json',"x-access-token":access_token},
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Product'])

    '''Test Get all sales'''

    def test_get_all_sales(self):
        access_token=self.get_user_token()
        response = self.app.get(
            '/api/v1/sales',
            headers={"content_type":'application/json',"x-access-token":access_token},
        )
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200, result['Sales Record'])

    ''' Test add new product'''

    def test_product_exist(self):
        access_token=self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales',
            headers={"content_type":'application/json',"x-access-token":access_token},
        )
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, result["Sales Record"])

    def test_add_new_sale_record(self):
        access_token=self.get_user_token()
        response = self.app.post(
            '/api/v1/sales',
            data=json.dumps(self.sales),
            headers={"content_type":'application/json',"x-access-token":access_token},
        )
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Sale Record'])

    '''Test fetch for specific sale record'''

    def test_fetch_single_sale_record(self):
        '''Test fetch for single sale record [GET request]'''
        access_token=self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales/1',
            headers={"content_type":'application/json',"x-access-token":access_token},
        )
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, result['Sale'])

    def test_items_outof_range_record(self):
        '''Test fetch for single sale record [GET request]'''
        access_token=self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales/2',
            headers={"content_type":'application/json',"x-access-token":access_token},
        )
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['Message'], 'Sale Not Found')
        self.assertEqual(resp.status_code, 400, result['Message'])

    '''Test invalid post url'''

    def test_invalid_post_product_url(self):
        response = self.app.post(
            '/api/v1/productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_invalid_get_product_url(self):
        response = self.app.get(
            '/api/v1//productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(response.status, '404 NOT FOUND')
