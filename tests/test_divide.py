# python -m unittest -v tests/test_divide.py

import unittest
from calc import aec_div

class TestSubtract(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(aec_div([20, 5]), 4)
        
    def test_limit_two_args(self):
        '''Need to fix this.'''
        self.assertRaises(TypeError, aec_div, [20, 4, 5]) 

if __name__ == '__main__':
	unittest.main()