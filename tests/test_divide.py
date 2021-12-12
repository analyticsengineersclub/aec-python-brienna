# python -m unittest -v tests/test_divide.py

import unittest
from calc import aec_div

class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(aec_div([20, 5]), 4)
        
    def test_limit_two_args(self):
        self.assertRaises(TypeError, aec_div, [20, 4, 5]) 

    def test_cant_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, aec_div, [20, 0])

if __name__ == '__main__':
	unittest.main()