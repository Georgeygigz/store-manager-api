from flask import abort, request,json
class Validate:
    def validate_empty_product_inputs(self,data):
        if (data['product_name'] == "") :
            abort(400, description="Product name required")
        if data['stock_amount'] == "":
            abort(400, description="Stock amount should not be empty")
        if data['low_inventory_stock'] == "":
            abort(400, description="low inventory stock field should not be empty")
        if data['price'] == "":
            abort(400, description="Price should not be empty")

    def validate_empty_sales_inputs(self,data):

        if data['product_name'] == "":
            abort(400, description="Product name should not be empty")
        if data['attedant_name'] == "":
            abort(400, description="Attedant name should not be empty")
        if data['customer_name'] == "":
            abort(400, description="Customer Name should not be empty")
        if data['quantity'] == "":
            abort(400, description="Quantity should not be empty")

    def validate_empty_users_inputs(self,data):
        if data['username'] == "":
            abort(400, description="Username should not be empty")
        if data['email'] == "":
            abort(400, description="Email should not be empty")
        if data['password'] == "":
            abort(400, description="Password should not be empty")
    
    def validate_correct_keys(self,data):
        if ( not data["product_name"] in request.json):
            abort(400, description="All field names required")