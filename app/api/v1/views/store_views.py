# app/api/v1/views/store_views.py

'''This is where all API Endpoints will be captured'''
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource

# local imports
from app.api.v1.models.store_model import Products, Sales, Users
from app.api.v1.views.auth_view import login_required
from app.api.v1.utils.utils import Validate


products = Products().get_all_products()
sales_record = Sales().get_all_sales()
all_users = Users().get_all_users()


class ViewProducts(Resource):
    '''Get all products'''
    @login_required
    def get(self, current_user):
        if not products:
            return make_response(jsonify({"Message": "No products available "}), 200)
        return make_response(jsonify({"Available Products": products}), 200)

    '''Adding a new product'''
    @login_required
    def post(self, current_user):

        data = request.get_json(force=True)
        Validate().validate_empty_product_inputs(data)
        Validate().validate_data_type(data)
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

        new_pro = Products()
        new_pro.insert_new_product(**new_product)

        return {"New Product": new_product}, 201  # created


'''Fetch single product'''


class ViewSingleProduct(Resource):
    @login_required
    def get(self, current_user, product_id):
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return {"Error": "Product Not Found"}, 400  # Not found
        return {"Product": single_product}, 200  # ok


'''View all sales records'''


class ViewSalesRecord(Resource):
    @login_required
    def get(self, current_user):
        if not sales_record:
            return {"Message": "No available sale records "}, 200  # ok
        return {"Sales Record": sales_record}, 200  # ok

    @login_required
    def post(self, current_user):
        current_date = str(date.today())
        data = request.get_json(force=True)
        Validate().validate_empty_sales_inputs(data)
        current_product = [
            product for product in products if product['product_name'] == request.json['product_name']]
        if not current_product or (current_product[0]['stock_amount'] == 0 or request.json['quantity'] > current_product[0]['stock_amount']):
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
        new_sales_record = Sales()
        new_sales_record.insert_new_sale(**new_sale)
        current_product[0]['stock_amount'] -= request.json['quantity']
        return {"New Sale Record": new_sale}, 201  # created


'''Fetch single sale record'''


class SingleSale(Resource):
    @login_required
    def get(self, current_user, sale_id):
        single_sale = [
            sale for sale in sales_record if sale['sale_id'] == sale_id]
        if single_sale:
            return {"Sale": single_sale}, 200  # ok
        return {"Message": "Sale Not Found"}, 400  # ok
