import unittest
from subtract import *

class TestSubtract(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(100, 50), 50)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)
        self.assertEqual(subtract(-5, -10), 5)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(10, 0), 10)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_floats(self):
        self.assertEqual(subtract(10.5, 2.3), 8.2)
        self.assertAlmostEqual(subtract(5.1, 2.1), 3.0)

    def test_subtract_large_numbers(self):
        self.assertEqual(subtract(1000000, 1), 999999)
