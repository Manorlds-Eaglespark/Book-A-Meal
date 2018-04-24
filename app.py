from flask import Flask, redirect, url_for, request, render_template, escape, session, flash
app = Flask(__name__)

# Add a meal in the system
@app.route('/add/meal')
def add_meal():
   return "Caterer gets a form to add a new meal"


# Modify a meal in the system
@app.route('/modify/meal/<int:mealID>')
def modify_meal():
   return "Caterer gets a form to modify meal with id: id"


# Delete a meal in the system
@app.route('/delete/meal/<int:mealID>')
def delete_meal():
   return "Caterer gets a prompt to delete meal with id: id"


# Add today's menu to the system
@app.route('/add/menu')
def add_menu():
   return "Caterer gets a form to add meals for that day"


# Get menu for the day
@app.route('/get/menu/<string:date>')
def today_menu():
   return "Customer gets a menu prepared for date: today"


# Add an order to the system
@app.route('/add/order')
def add_order():
   return "Customer makes an order from the meal options in the order"


# Get all orders for a specific day
@app.route('/get/orders/<string:date>')
def all_orders_date():
   return "Caterer can view all the orders that came through today"


# Modify an order
@app.route('/modify/order/<int:orderID>/<int:customerID>')
def modify_order():
   return "Customer gets a form where they can modify an order they already made"



if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)