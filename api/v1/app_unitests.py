
import unittest
import base64
from flask import Flask
from flask_httpauth import HTTPBasicAuth
import app.py


class HTTPAuthTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'my secret'

        basic_auth = HTTPBasicAuth()

        @basic_auth.get_password
        def get_basic_password(username):
            if username == 'john':
                return 'hello'
            elif username == 'susan':
                return 'bye'
            else:
                return None

        @app.route('/')
        def index():
            return 'index'

        @app.route('/basic')
        @basic_auth.login_required
        def basic_auth_route():
            return 'basic_auth:' + basic_auth.username()

        self.app = app
        self.basic_auth = basic_auth
        self.client = app.test_client()




def test_signup(self):
        response = self.client.get('/auth/signup')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('Created' in response.headers)

def test_remove_meal(self):
        response = self.client.get('/meals/<mealId>')
        self.assertTrue(type(response, string)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(challenge(10), list))
        


if __name__ == '__main__':
    app.run()