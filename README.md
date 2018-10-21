# store-manager-api
This is a Store Manager Web Application

[![Build Status](https://travis-ci.com/Georgeygigz/store-manager-api.svg?branch=bg-validation-161336793)](https://travis-ci.com/Georgeygigz/store-manager-api)  [![Coverage Status](https://coveralls.io/repos/github/Georgeygigz/store-manager-api/badge.svg?branch=bg-validation-161336793)](https://coveralls.io/github/Georgeygigz/store-manager-api?branch=master)   [![Maintainability](https://api.codeclimate.com/v1/badges/e7f6ace7b0d4ccb54c73/maintainability)](https://codeclimate.com/github/Georgeygigz/store-manager-api/maintainability)

# This challenge creates a set of API Endpoints listed below
| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v1/products | Get all the products| GET |
| api/v1/products | Add a new product| POST |
| api/v1/products/product_id| Fetch single product |GET|
| api/v1/sales | Fetch all sales record |GET|
| api/v1/sales | Makes a new sales record |POST|
| api/v1/sales/sale_id |Fetch single sale record|GET|
| api/v1/auth/register | Makes a new user account |POST|
| api/v1/auth/login|User login |POST|

## TOOLS TO BE USED IN THE CHALLENGE
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)

**How to run the application**
 1. Make a new directory on your computer
 2. Open the terminal and navigate to the folder
 3. `git clone` this  <code>[repo](https://github.com/Georgeygigz/store-manager-api/)</code>
 4.  run `pip install -r requirements.txt` to install the dependencies
 5.  Then on your terminal write ```flask run.py``` to start the server
 6. Then on [postman](https://www.getpostman.com/), navigate to this url `api/v1/auth/login`

 # How to test the Api Endpoints Locally

 1. [Postman](https://www.getpostman.com/) is used to input data and get the output

 2. After starting the Postman, The following url are used to navigate to the Api Endpoints

 3. To list all products use this url <code>http://127.0.0.1:5000/api/v1/products</code> ensure you select    _GET_ request

 4. To Place add a new product use this url <code>http://127.0.0.1:5000/api/v1/products</code> and select _POST_
         
         This is an example of a new order to be placed
                   {         
                        "product_name": "orange",
                        "category_id": 1,
                        "stock_amount": 200,
                        "price": 22,
                        "low_inventory_stock": 4
            
                    }
  
  5. To get a specific product user this url <code>http://127.0.0.1:5000/ api/v1/products/`<int:product_id>`</code> and select _GET_

  6. To make a new sale record user This URL <code>http://127.0.0.1:5000/api/v1/sales</code> and select _POST_
      ```
      Example 
      
         {           
            "attedant_name": "George",
            "customer_name": "mary",
            "product_name":"orange",
            "quantity": 20
           }
      ```
  7. To list all sales records use this url <code>http://127.0.0.1:5000/api/v1/sales</code> ensure you select    _GET_ request

  8. To get a specific product user this url <code>http://127.0.0.1:5000/api/v1/sales/sale_id></code> and select _GET_ request

  9. To  create a new user user This URL <code>http://127.0.0.1:5000/api/v1/auth/register</code> and select _POST_
      ```
      Example 
      
            {           
                "username": "george",
                "email": "george@gmail.com",
                "password":"g@#$4HDKD",
                "role": "user"
             }
      ``` 
  9. User can use this URL to login <code>http://127.0.0.1:5000/api/v1/auth/login</code> and select _POST_
      ```
      Example 
      
           {      
               
                "email": "george@gmail.com",
                "password":"g@#$4HDKD"

            }
      ``` 

# How to run the application on heroku

 Navigate to this [link](https://gigzstoremanager-api-heroku.herokuapp.com/api/v1/products) to run my application on heroku

 # View on postman documentation

 [Postman documentation](https://documenter.getpostman.com/view/5283750/RWguwcEB#intro)

# Author
`Georgey Gigz`

# Realease 
 Version one `(v1)`