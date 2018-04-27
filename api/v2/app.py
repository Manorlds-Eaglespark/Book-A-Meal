
from flask import Flask, jsonify

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
        'mealId': 4,
        'userId': 27,
        'time_created': 'Monday, 14th February 2018'
    },
    {
        'id': 2,
        'mealId': 7,
        'userId': 34,
        'time_created': 'Monday, 14th February 2018'
    }
]

menu = [
    {
        'id': 1,
        'mealIds': '4,2,5,6,7',
        'userId': 27,
        'date': 'Monday, 14th February 2018'
    }
]





@app.route('/meals/', methods=['GET'])
def get_tasks():
    return jsonify({'meals': meals})

# Get all the orders 
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})
   
# Get menu for the day
@app.route('/menu/', methods=['GET'])
def get_menu():
    return jsonify({'menu': menu})

if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)

