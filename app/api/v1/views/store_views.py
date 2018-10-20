# app/api/v1/views/store_views.py

'''This is where all API Endpoints will be captured'''
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource

# local imports
from app.api.v1.models.store_model import StoreManager
from app.api.v1.views.auth_view import login_required
from app.api.v1.utils.utils import Validate


products = StoreManager().get_all_products()
sales_record = StoreManager().get_all_sales()




class ViewProducts(Resource):
    '''Get all products'''

    def get(self):
        return make_response(jsonify({"Available Products": products}), 200)

    '''Adding a new product'''

    def post(self):

        data = request.get_json(force=True)
        Validate().validate_empty_product_inputs(data)
        product_id = len(products)+1
        product_name = data["product_name"]
        category = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
        inventory_stock = data['low_inventory_stock']
        product = [product for product in products if product['product_name']
                   == request.json['product_name']]
        if (not request.json or not "product_name" in request.json):
            return {'Error': "Request Not found"}, 400  # not found

        if type((request.json['stock_amount']) or (request.json['price'])) not in [int, float]:
            return {"Error": "Require int or float type"}

        if request.json['product_name'] in [n_product['product_name'] for n_product in products]:
            product[0]["stock_amount"] += request.json['stock_amount']
            return {"Products": product}, 200  # ok

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "category_id": category,
            "stock_amount": stock_amount,
            "price": price,
            "low_inventory_stock": inventory_stock
        }

        products.append(new_product)

        return {"New Product": new_product}, 201  # created


'''Fetch single product'''


class ViewSingleProduct(Resource):
    def get(self, product_id):
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return {"Error": "Product Not Found"}, 400  # Not found
        return {"Product": single_product}, 200  # ok


'''View all sales records'''


class ViewSalesRecord(Resource):
    def get(self):
        return {"Sales Record": sales_record}, 200  # ok

    def post(self):
        current_date = str(date.today())
        data = request.get_json(force=True)
        Validate().validate_empty_sales_inputs(data)
        current_product = [
            product for product in products if product['product_name'] == request.json['product_name']]
        if not current_product or current_product[0]['stock_amount'] == 0:
            return {"Message": "{} Out of stock, Please add {} in stock beforemaking a sale".format(request.json['product_name'], request.json['product_name'])}, 200
        sale_id = len(sales_record)+1
        attedant_name = data["attedant_name"]
        customer_name = data["customer_name"]
        product_name = data["product_name"]
        price = current_product[0]['price']
        quantity = data["quantity"]
        total_price = price*quantity
        date_sold = current_date

        if (not request.json or not "product_name" in request.json):
            return {'Error': "Request Not found"}, 400  # not found

        if request.json['product_name'] in [sale['product_name'] for sale in sales_record]:
            # ok
            return {"Message": "{} Exist in cart".format(request.json['product_name'])}, 200

        new_sale = {
            "sale_id": sale_id,
            "attedant_name": attedant_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "product_price": price,
            "quantity": quantity,
            "total_price": total_price,
            "date_sold": date_sold
        }


        sales_record.append(new_sale)
        current_product[0]['stock_amount'] -= request.json['quantity']
        return {"New Sale Record": new_sale}, 201  # created


'''Fetch single sale record'''


class SingleSale(Resource):

    def get(self, sale_id):
        single_sale = [
            sale for sale in sales_record if sale['sale_id'] == sale_id]
        if single_sale:
            return {"Sale": single_sale}, 200  # ok
        return {"Message": "Sale Not Found"}, 400  # ok
