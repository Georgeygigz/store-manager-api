#app/api/v1/models/store_model.py

'''Data Structre model that act as the database'''

all_products = []
all_sales = []
all_users = [] 
class Products():  
    def __init__(self, product_id=1,product_name="Orange",category_id="fruits",stock_amount=10,price=20,low_inventory_stock=2):
        self.product_id=product_id
        self.product_name=product_name
        self.category_id=category_id
        self.stock_amount=stock_amount
        self.price=price
        self.low_inventory_stock=low_inventory_stock
    
    def get_all_products(self):
        return all_products

    def insert_new_product(self):
        new_product={
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category_id": self.category_id,
            "stock_amount": self.stock_amount,
            "price": self.price,
            "low_inventory_stock": self.low_inventory_stock
        }
        all_products.append(new_product)



class Sales:
    def __init__(self, sale_id=1,attedant_name="Orange",customer_name="fruits",product_name=10,product_price=20,quantity=2,total_price=300,date_sold="2018-2-22"):
        self.sale_id=sale_id
        self.attedant_name =attedant_name
        self.customer_name=customer_name
        self.product_name=product_name
        self.product_price=product_price
        self.quantity=quantity
        self.total_price=total_price
        self.date_sold=date_sold
    
    def get_all_sales(self):
        return all_sales

    def insert_new_sale(self):
        new_sale={
            "sale_id": self.sale_id,
            "attedant_name": self.attedant_name,
            "customer_name": self.customer_name,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "date_sold": self.date_sold
        }
        all_sales.append(new_sale)

class Users:
    def __init__(self, user_id=1,username="geore",email="georgey@gmail.com",password="pass",role="attendant"):
        self.user_id=user_id
        self.username =username
        self.email=email
        self.password=password
        self.role=role
    
    def get_all_users(self):
        return all_users

    def insert_new_user(self):
        new_user={"user_id": self.user_id,
                  "username": self.username,
                  "email": self.email,
                  "password": self.password,
                  "role": self.role}
        all_users.append(new_user)
