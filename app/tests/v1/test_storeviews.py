#app/tests/v1/test_storeviews
import unittest
import json
from app import create_app

'''
Creating a new testing  class
'''
class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app=create_app().test_client()
        self.app.testing = True
        self.products={"product_id":1,
                       "product_name":"Bread",
                       "category_id":1,
                       "stock_amount":2000,
                       "price":20}
        
    '''
    Test Get all products
    '''
    def test_get_all_products(self):
        response=self.app.get('/api/v1/products',
                                headers={'content_type': 'application/json'})
        self.assertEqual(response.status_code,200)