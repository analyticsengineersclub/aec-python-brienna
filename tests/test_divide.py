# python -m unittest -v tests/test_divide.py

import unittest
from calc import aec_div

class TestSubtract(unittest.TestCase):

	def test_divide(self):
		self.assertEqual(aec_div([20, 5]), 4)

if __name__ == '__main__':
	unittest.main()