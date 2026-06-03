import unittest
from divide_by_subtract import *

class TestDivide(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide_by_subtract(10, 2), 5)
        self.assertEqual(divide_by_subtract(20, 4), 5)
        self.assertEqual(divide_by_subtract(7, 3), 2)

    def test_divide_with_zero(self):
        self.assertEqual(divide_by_subtract(0, 5), 0)
        self.assertEqual(divide_by_subtract(0, -5), 0)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide_by_subtract(-10, 2), -5)
        self.assertEqual(divide_by_subtract(10, -2), -5)
        self.assertEqual(divide_by_subtract(-10, -2), 5)

    def test_divide_by_one(self):
        self.assertEqual(divide_by_subtract(15, 1), 15)
        self.assertEqual(divide_by_subtract(-15, 1), -15)

    def test_divide_large_numbers(self):
        self.assertEqual(divide_by_subtract(1000000, 1000), 1000)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide_by_subtract(10, 0)
        with self.assertRaises(ValueError):
            divide_by_subtract(-5, 0)

    def test_divide_small_divisor(self):
        self.assertEqual(divide_by_subtract(5, 10), 0)
        self.assertEqual(divide_by_subtract(-5, 10), 0)


if __name__ == '__main__':
    unittest.main()