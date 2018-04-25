from flask import Flask, redirect, url_for, request, render_template, escape, session, flash
import random
import time
app = Flask(__name__)

#we need a User object, this object will represent the Customers and Restaurant caterers who will be using the application
class User:
   id 
   name 
   email 
   admin_status 
   time_created   
   #Constructor for the User object, for initialization
   def __init__(self, name, email):
      self.id = random.randint(1001)
      self.name = name
      self.email = email
      self.admin_status = "false"
      self.time_created = time.time()

#Customers will be ordering meal instances whose ids will be added to the ordered items for customers
class Meal:
   id 
   name 
   price 
   time_created = 0.0 
   #Constructor
   def __init__(self, name, price):
      self.id = random.randint(1001)
      self.name = name
      self.price = price
      self.time_created = time.time()



#We will record the meal option selected and by who in this object
class Order:
   id
   mealId           #the meal which was ordered
   userId           #the person that ordered the meal
   time_created     #time the meal was ordered
   
   #constructor
   def __init__(self, mealId, userId):
      self.id = random.randint(1001)
      self.mealId = mealId
      self.userId = userId
      self.time_created = time.time()

#Menu object will just be an object to help us hold meal Ids selected for today's serving
#MealIds is a string made from a string of meal ids separated by commas e.g "10,5,6,18" 
class Menu:
   id 
   mealIds
   date 
   
   def __init__(self, mealIds):
      self.id = random.randint(1001)
      self.mealIds = mealIds
      self.time_created = time.time()

      
#We save exception and return error page for every view. 
#It is a lot of work to write this code everywhere. 
#Flask provides a method to do this. So we define an errorhandler method like this.
      
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

# For this commit, lemme list the routes we need for the api, to which next we will build unittests

# Register a user
@app.route('/auth/signup')


# Login a user
@app.route('/auth/login')

# Get all the meal options
@app.route('/meals/')

# Add a meal option
@app.route('/meals/ ')


# Update the information of a meal option
@app.route('/meals/<int:mealId>')

# Remove a meal option
@app.route('/meals/<int:mealId>')


# Setup the menu for the day 
@app.route('/menu/')


# Get the menu for the day
@app.route('/menu/')


# Select the meal option from the menu
@app.route('/orders')

# Modify an order
@app.route('/orders/<int:orderId>')

# Get all the orders 
@app.route('/orders')



if __name__ == "__main__":
    app.run(host='localhost', port=5003, debug=False)
