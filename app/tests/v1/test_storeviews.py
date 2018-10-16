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
        self.sales={"sale_id":1,
                    "attedant_name":"Mary",
                    "product_name":"Bread",
                    "product_price":20,
                    "quantity":3,
                    "total_price":60,
                    "date_sold":"12-3-2018"}
        
    '''
    Test Get all products
    '''
    def test_get_all_products(self):
        response=self.app.get('/api/v1/products',
                                headers={'content_type': 'application/json'})
        self.assertEqual(response.status_code,200)
    
    '''
    Test add new product
    '''
    def test_add_new_product(self):
        response=self.app.post('/api/v1/products',
                               data=json.dumps(self.products),
                               headers={'content_type': 'application/json'})

        self.assertEqual(response.json,{'New Product': {"category_id": 1,'price': 20,'product_id': 1,'product_name': 'Bread','stock_amount': 2000}}) 
        self.assertEqual(response.status_code,201)

    '''Test fetch for specific product'''
    def test_fetch_single_product(self):
        '''Test fetch for single product [GET request]'''
        
        result=self.app.get('/api/v1/products/1',
                            headers={'content_type': 'application/json'})
        self.assertEqual(result.status_code,200)
    
    '''
    Test Get all sales
    '''
    def test_get_all_sales(self):
        response=self.app.get('/api/v1/sales',
                                headers={'content_type': 'application/json'})
        self.assertEqual(response.status_code,200)
    
    
    '''
    Test add new product
    '''
    def test_make_new_sale_record(self):
        response=self.app.post('/api/v1/sales',
                               data=json.dumps(self.sales),
                               headers={'content_type': 'application/json'})

        self.assertEqual(response.json,{'New Sale Record':
                                        {"sale_id":1,
                                        "attedant_name":"Mary",
                                        "product_name":"Bread",
                                        "product_price":20,
                                        "quantity":3,
                                        "total_price":60,
                                        "date_sold":"2018-10-16"}}) 
        self.assertEqual(response.status_code,201)