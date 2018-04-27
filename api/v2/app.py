
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
        'time_created': 'Monday, 14th February 2018'
    },
    {
        'id': 2,
        'mealId': 7,
        'time_created': 'Monday, 14th February 2018'
    }
]


order = [
    {
        'id': 1,
        'mealId': 4,
        'time_created': 'Monday, 14th February 2018'
    }
]

menu = [
    {
        'id': 1,
        'mealIds': '4,2,5,6,7',
        'date': 'Monday, 14th February 2018'
    }
]




@app.route('/auth/signin', methods=['POST'])
def login(self, username, password):
    return self.app.post('/auth/signin', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

   

@app.route('/auth/signup', methods=['POST'])
def main():
   url = request.form.get('return_url')
   # just example. will return value of sent return_url
   return Response(
      response=json.dumps({'return_url': url}),
      status_code = 201,
      content_type='application/json'
   )



# Select the meal option from the menu
@app.route('/orders/<int:orderId>', methods=['GET'])
def select_order(orderId):
    return jsonify({'order': order})


@app.route('/meals/', methods=['GET'])
def get_tasks():
    return jsonify({'meals': meals})


# Get all the orders 
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

   # Update the information of a meal option
@app.route('/meals/<int:mealId>', methods=['PUT'])
def update_meal(mealId):
   
    if request.method =='PUT':

        name = request.form['name']

        price = request.form['price']

        time_created = request.form['time_created']

        #creates users with above credentials  

        return jsonify({'status':'New user created'}), 202



@app.route('/auth/signup', methods=['POST'])

def signup():

    """method implementing signup"""

    if request.method =='POST':

        name = request.form['name']

        email = request.form['email']

        password = request.form['password']

        #create user with above credentials

        return jsonify({'status':'new user added'}), 201

      
    
# Get menu for the day
@app.route('/menu/', methods=['GET'])
def get_menu():
    return jsonify({'menu': menu})


# Setup the menu for the day 
@app.route('/menu/', methods=['POST'])

def create_menu():

    """method implementing signup"""

    if request.method =='POST':

        mealIds = request.form['mealIds']

        date = request.form['date']

        #create menu with above credentials

        return jsonify({'status':'You have set the menu for today'}), 201


if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)

