import unittest
from app import signup
 
class TddInFlaskAndelaTia(unittest.TestCase):
 
    def test_route_method_1(self):
        self.assertEqual(signup(), "New Account created")
        self.assertNotEqual(signup(), "")
        
 
 
if __name__ == '__main__':
    unittest.main()