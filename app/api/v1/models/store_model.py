'''
Data Structre model that act as the database
'''
class StoreManager():
    def __init__(self):
        self.all_products=[]
        self.all_sales=[]

    
    def get_all_products(self):
        return self.all_products
    
    def get_all_sales(self):
        return self.all_sales


