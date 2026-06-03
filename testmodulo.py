import unittest
from modulo import *

class TestModulo(unittest.TestCase):

    def test_modulo_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 6), 2)
        self.assertEqual(modulo(15, 5), 0)

    def test_modulo_with_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)
        self.assertEqual(modulo(0, -7), 0)


    def test_modulo_large_numbers(self):
        self.assertEqual(modulo(1000000, 7), 1)

    def test_modulo_by_one(self):
        self.assertEqual(modulo(25, 1), 0)
        self.assertEqual(modulo(-25, 1), 0)

    def test_modulo_division_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)
        with self.assertRaises(ValueError):
            modulo(-15, 0)



