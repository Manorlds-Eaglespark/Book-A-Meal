
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

@app.route('/meals/', methods=['GET'])
def get_tasks():
    return jsonify({'meals': meals})

if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)

