import unittest
import app
import requests
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
       

    def test_all_meals(self):
        response = self.app.get('/meals/')
        data = json.loads(response.data)
        self.assertEqual(data['meals'], [
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
        ])
        self.assertEqual(response.status_code, 200)


    def test_orders(self):
        response = self.app.get('/orders')
        data = json.loads(response.data)
        self.assertEqual(data['orders'], [
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
        ])
        self.assertEqual(response.status_code, 200)


    def test_today_menu(self):
        response = self.app.get('/menu/')
        data = json.loads(response.data)
        self.assertEqual(data['menu'], [
                {
                    'id': 1,
                    'mealIds': '4,2,5,6,7',
                    'userId': 27,
                    'date': 'Monday, 14th February 2018'
                }
                
        ])
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
