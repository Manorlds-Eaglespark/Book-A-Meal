
from flask import Flask, jsonify, request
import time

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
            name = str(request.get_json().get('name'))
            email = str(request.get_json().get('email'))
            password = str(request.get_json().get('password'))
            if name:
               if email:
                   if password:

                            response = jsonify({
                                'name': name,
                                'email': email
                            })
                            response.status_code = 201
                            return response


# Select the meal option from the menu
@app.route('/orders/<int:orderId>', methods=['GET'])
def select_order(orderId):
    return jsonify({'order': order})


# Get all the meal options
@app.route('/meals/', methods=['GET'])
def get_meals():
    return jsonify({'meals': meals})




# Add a meal option
@app.route('/meals/', methods=['POST'])
def add_a_meal():
            name = str(request.get_json().get('name'))
            price = str(request.get_json().get('price'))
            time_created = str(request.get_json().get('time_created'))
            if name:
               if price:
                   if time_created:
                            response = jsonify({
                                'name': name,
                                'price': price,
                                'time_creatd': time.asctime( time.localtime(time.time()) )
                            })
                            response.status_code = 201
                            return response




# Get all the orders 
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})


# Make an order 
@app.route('/orders', methods=['POST'])
def make_order():
            meal_id = request.get_json().get('meal_id')
            user_id = request.get_json().get('user_id')

            if meal_id:
               if user_id:
                            response = jsonify({
                                'meal_id': meal_id,
                                'user_id': user_id,
                                'Expiration time': time.asctime( time.localtime( time.time()  + 600 ))
                            })
                            response.status_code = 201
                            return response


    
# Get menu for the day
@app.route('/menu/', methods=['GET'])
def get_menu():
    return jsonify({'menu': menu})


# Setup the menu for the day 
@app.route('/menu/', methods=['POST'])
def create_menu():
            meal_ids = str(request.get_json().get('meal_ids'))
            if meal_ids:
                    response = jsonify({
                        'meal_ids': meal_ids,
                        'time_created': time.asctime( time.localtime(time.time()) )
                    })
                    response.status_code = 201
                    return response



if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)

