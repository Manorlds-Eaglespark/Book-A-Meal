# test_bucketlist.py
import unittest
import os
import json
from run import signup
from app import create_app

class TddInFlaskAndelaTia(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        #self.bucketlist = {'name': 'Go to Borabora for vacation'}
        

    def test_signup(self):
        res = self.client().post('/auth/signup', data=signup())
        self.assertEqual(res.status_code, 201)
        self.assertIn('New account', str(res.data))

   

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
