from flask import Flask, redirect, url_for, request, render_template, escape, session, flash
import random
import time
app = Flask(__name__)

class User:
   id = 0
   name =  ""
   email = ""
   time_created = 0.0 
   
   def __init__(self, name, email):
      self.id = random.randint(1001)
      self.name = name
      self.email = city
      self.time_created = time.time()


class Meal:
   id = 0
   name =  ""
   price = ""
   time_created = 0.0 
   
   def __init__(self, name, price):
      self.id = random.randint(1001)
      self.name = name
      self.price = price
      self.time_created = time.time()




class Order:
   id = 0
   mealId =  0
   userId = 0
   time_created = 0.0 
   
   def __init__(self, mealId, userId):
      self.id = random.randint(1001)
      self.mealId = name
      self.userId = city
      self.time_created = time.time()


#MealIds is a string made from a string of meal ids separated by commas e.g "10,5,6,18" 
class Menu:
   id = 0
   mealIds =  ""
   date = ""
   
   def __init__(self, mealIds):
      self.id = random.randint(1001)
      self.mealIds = mealIds
      self.time_created = time.time()


@app.errorhandler(400)
def internal_error(exception):
        app.logger.error(exception)
        return "Bad Request: The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications."


@app.errorhandler(401)
def internal_error(exception):
        app.logger.error(exception)
        return "Unauthorized: The request requires user authentication."


@app.errorhandler(404)
def internal_error(exception):
        app.logger.error(exception)
        return "Not Found: The server has not found anything matching the Request-URI."

@app.errorhandler(500)
def internal_error(exception):
        app.logger.error(exception)
        return "Internal Server Error: The server encountered an unexpected condition which prevented it from fulfilling the request."   


@app.errorhandler(503)
def internal_error(exception):
        app.logger.error(exception)
        return "Service Unavailable: The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."    


# Register a user
@app.route('/auth/signup')
def signup():
   return "1"


# Login a user
@app.route('/auth/login')
def login():
   return "2"


# Get all the meal options
@app.route('/meals/')
def all_meals():
   return "3"


# Add a meal option
@app.route('/meals/ ')
def add_meal():
   return "4"


# Update the information of a meal option
@app.route('/meals/<mealId>')
def update_meal():
   return "5"


# Remove a meal option
@app.route('/meals/<int:mealId>')
def remove_meal():
   return "6"


# Setup the menu for the day 
@app.route('/menu/')
def set_today_menu():
   return "7"


# Get the menu for the day
@app.route('/menu/')
def today_menu():
   return "8"


# Select the meal option from the menu
@app.route('/orders')
def select_order():
   return "9"


# Modify an order
@app.route('/orders/orderId')
def modify_order():
   return "10"


# Get all the orders 
@app.route('/orders')
def orders():
   return "11"



if __name__ == "__main__":
    app.run(host='localhost', port=5003, debug=False)
