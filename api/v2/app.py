"""This is the API file for the Book-A-Meal application"""
import time
from flask import Flask, jsonify, request


app = Flask(__name__)

meals = [
    {
        'id': 1,
        'name': 'Beef and Rice',
        'price': '25000',
        'time_created': 'Monday, 14th February 2018'
    },
    {
        'id': 2,
        'name': 'Chicken and Matooke',
        'price': '35000',
        'time_created': 'Monday, 14th February 2018'
    }
]

orders = [
    {
        'id': 1,
        'user_id': 10,
        'meal_id': 4,
        'time_created': 'Monday, 14th February 2018'
    },
    {
        'id': 2,
        'user_id': 11,
        'meal_id': 7,
        'time_created': 'Monday, 14th February 2018'
    }
]

order = [
    {
        'id': 1,
        'meal_id': 4,
        'time_created': 'Monday, 14th February 2018'
    }
]

menu = [
    {
        'id': 1,
        'meal_ids': '4,2,5,6,7',
        'time_created': 'Monday, 14th February 2018'
    }
]




#Save a new user to make a signup
@app.route('/auth/signup', methods=['POST'])
def signup():
    """Method for creation of new user on the system"""
    name = str(request.get_json().get('name'))
    email = str(request.get_json().get('email'))
    password = str(request.get_json().get('password'))
    if name and email and password:
        response = jsonify({
            'name': name,
            'email': email
            })
        response.status_code = 201
        return response
    #return None


@app.route('/orders/<int:order_id>', methods=['GET'])
def select_order(order_id):
    """Method that selects a meal to an order"""
    return jsonify({'order': order_id})


@app.route('/meals/', methods=['GET'])
def get_meals():
    """This method returns all meals stored in the system"""
    return jsonify({'meals': meals})




@app.route('/meals/', methods=['POST'])
def add_a_meal():
    """A Method to add a meal to the system"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))
    time_created = str(request.get_json().get('time_created'))
    if name and price and time_created:
        response = jsonify({
            'name': name,
            'price': price,
            'time_creatd': time.asctime(time.localtime(time.time()))
            })
        response.status_code = 201
        return response
    #return None


@app.route('/orders', methods=['GET'])
def get_orders():
    """A Method that returns all the orders made"""
    return jsonify({'orders': orders})


@app.route('/orders', methods=['POST'])
def make_order():
    """A Method to make a new Order"""
    meal_id = request.get_json().get('meal_id')
    user_id = request.get_json().get('user_id')
    if meal_id and user_id:
        response = jsonify({
            'meal_id': meal_id,
            'user_id': user_id,
            'Expiration time': time.asctime(time.localtime( \
            time.time()  + 600))
            })
        response.status_code = 201
        return response
    #return None


@app.route('/order/<int:order_id>', methods=['PUT'])
#def modify_order(order_id):
def modify_order():
    """Method to modify an Order"""
    meal_id = str(request.get_json().get('meal_id'))
    response = jsonify({
        'new meal_id': meal_id,
        'date_created': "original created time",
        'date_updated': time.asctime(time.localtime(time.time()))
        })
    response.status_code = 200
    return response


@app.route('/menu/', methods=['GET'])
def get_menu():
    """A Method to return the menu for the day"""
    return jsonify({'menu': menu})


@app.route('/menu/', methods=['POST'])
def create_menu():
    """Method to create a menu for that day"""
    meal_ids = str(request.get_json().get('meal_ids'))
    if meal_ids:
        response = jsonify({
            'meal_ids': meal_ids,
            'time_created': time.asctime(time.localtime(time.time()))
            })
        response.status_code = 201
        return response
    #return None



if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)
    