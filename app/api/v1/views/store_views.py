#app/api/v1/views/store_views.py
'''
This is where all API Endpoints will be captured
'''
from flask import request
from flask_restful import Resource

#import class products
from app.api.v1.models.store_model import Products


products=Products().get_all_products()

class ViewProducts(Resource):
    '''Get all products'''
    def get(self):
        return {"Available Products":products},200
    
    '''Adding a new product'''
    def post(self):
        data=request.get_json(force=True)
        product_id=len(products)+1
        product_name=data["product_name"]
        category=data["category"]
        stock_amount=data["stock_amount"]
        price=data['price']
        product=[product for product in products if product['product_name']==request.json['product_name']]
        if type((request.json['stock_amount']) or (request.json['price'])) not in [int,float]:
            return {"Error":"Require int or float type"}

        if request.json['product_name'] in [n_product['product_name'] for n_product in products]:
            product[0]["stock_amount"]+=request.json['stock_amount']
            return {"Products":product}
        
        new_product={"product_id":product_id,
                     "product_name":product_name,
                     "category":category,
                     "stock_amount":stock_amount,
                     "price":price}
        
        products.append(new_product)

        return {"New Product":new_product},201 #created
