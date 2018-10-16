#app/tests/v1/test_models.py
'''
 Test case for our data storage
'''
import unittest
from app import create_app
from app.api.v1.models.store_model import StoreManager

class TestProductsModels(unittest.TestCase):
    '''Test for products class  and methods'''
    def setUp(self):
        '''Set up the model.'''
        self.products=StoreManager()

    '''
    Test for available records
    '''
    def test_available_data(self):
        self.assertEqual(self.products.get_all_products(),[])
        self.assertEqual(self.products.get_all_sales(),[])
        self.assertEqual(self.products.get_all_admin_users(),[])
        self.assertEqual(self.products.get_all_store_attedant(),[])
