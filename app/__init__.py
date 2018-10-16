#app/__init__.py
'''
Register Blueprints
'''
from flask import Flask,Blueprint
from flask_restful import Api


#local imports
from app.api.v1.views.store_views import ViewProducts,ViewSingleProduct,ViewSalesRecord
from instance.config import app_configuration

blueprint=Blueprint('product',__name__,url_prefix='/api/v1')
app_api=Api(blueprint)

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_configuration['development'])
    app.register_blueprint(blueprint)
    app_api.add_resource(ViewProducts,'/products')
    app_api.add_resource(ViewSingleProduct,'/products/<int:product_id>')
    app_api.add_resource(ViewSalesRecord,'/sales')
    return app
