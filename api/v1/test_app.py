import unittest
from app import signup, remove_meal
 
class TddInFlaskAndelaTia(unittest.TestCase):
 
    def test_route_method_1(self):
        self.assertEqual(signup(), "New Account created")
        self.assertNotEqual(signup(), "")
       
        
        self.assertIn("10", remove_meal(10))
        
 
 
if __name__ == '__main__':
    unittest.main()
