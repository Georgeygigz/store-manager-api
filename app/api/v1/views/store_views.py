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
    def get(self):
        return {"Available Products":products},200