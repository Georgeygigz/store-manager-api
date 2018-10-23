#app/api/v1/models/store_model.py

'''Data Structre model that act as the database'''
all_users = [] 
all_products = []
all_sales = []
class Products():  
    def __init__(self):
        self.all_products =all_products
    
    def get_all_products(self):
        return self.all_products

    def insert_new_product(self,  product_id,product_name,category_id,stock_amount,price,low_inventory_stock):
        new_product={
            "product_id": product_id,
            "product_name": product_name,
            "category_id": category_id,
            "stock_amount":stock_amount,
            "price": price,
            "low_inventory_stock": low_inventory_stock
        }
        self.all_products.append(new_product)



class Sales:
    def __init__(self):
        self.all_sales =all_sales
    
    def get_all_sales(self):
        return self.all_sales

    def insert_new_sale(self ,sale_id,attedant_name,customer_name,product_name,product_price,quantity,total_price,date_sold):
        new_sale={
            "sale_id": sale_id,
            "attedant_name": attedant_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "product_price": product_price,
            "quantity": quantity,
            "total_price": total_price,
            "date_sold": date_sold
        }
        self.all_sales.append(new_sale)

class Users:
    def __init__(self):
        self.all_users =all_users 
    
    def get_all_users(self):
        return self.all_users

    def insert_new_user(self, user_id,username,email,password,role):
        new_user={"user_id": user_id,
                  "username":username,
                  "email": email,
                  "password": password,
                  "role": role}
        self.all_users.append(new_user)
