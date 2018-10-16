#app/api/v1/views/store_views.py
'''
This is where all API Endpoints will be captured
'''
from flask import request
from datetime import date
from flask_restful import Resource

#import class products
from app.api.v1.models.store_model import StoreManager


products=StoreManager().get_all_products()
sales_record=StoreManager().get_all_sales()
class ViewProducts(Resource):
    '''Get all products'''
    def get(self):
        return {"Available Products":products},200
    
    '''Adding a new product'''
    def post(self):
       
        data=request.get_json(force=True)
        product_id=len(products)+1
        product_name=data["product_name"]
        category=data["category_id"]
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
                     "category_id":category,
                     "stock_amount":stock_amount,
                     "price":price}
        
        products.append(new_product)

        return {"New Product":new_product},201 #created

'''Fetch single product'''
class ViewSingleProduct(Resource):
        def get(self,product_id):
            single_product=[product for product in products if product['product_id']==product_id]
            if not single_product:
                return {"Error":"Product Not Found"}
            return {"Product":single_product},200

'''View all sales records'''
class ViewSalesRecord(Resource):
    def get(self):
        return {"Sales Record":sales_record},200
    
    def post(self):
        current_date=str(date.today())
        data=request.get_json(force=True)
        sale_id=len(sales_record)+1
        attedant_name=data["attedant_name"]
        product_name=data["product_name"]
        price=data["product_price"]
        quantity=data["quantity"]
        total_price=price*quantity
        date_sold=current_date

        if request.json['product_name'] in  [sale['product_name'] for sale in sales_record]:
            return {"Message":"{} Exist in cart".format(request.json['product_name'])}

        new_sale={"sale_id":sale_id,
                  "attedant_name":attedant_name,
                  "product_name":product_name,
                  "product_price":price,
                  "quantity":quantity,
                  "total_price":total_price,
                  "date_sold":date_sold}
        product_sold=[product for product in products if product['product_name']==request.json['product_name']]
        if not product_sold or product_sold[0]['stock_amount']==0:
            return {"Message":"{} Out of stock".format(request.json['product_name'])}
        sales_record.append(new_sale)
        product_sold[0]['stock_amount']-=request.json['quantity']
        return {"New Sale Record":new_sale},201


'''Fetch single sale record'''
class SingleSale(Resource):
    def get(self,sale_id):
        single_sale=[sale for sale in sales_record if sale['sale_id']==sale_id]
        if not single_sale:
            return {"Message":"Sale Not Found"}
        return {"Sale":single_sale},200 #ok
            
