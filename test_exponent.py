import unittest
from exponent import exponent
class TestExponent(unittest.TestCase):
    def test_exponent_one(self):
        assert exponent(2, 3) == 8

    def test_exponent_zero_power(self):
        assert exponent(5, 0) == 1

    def test_exponent_one_power(self):
        assert exponent(7, 1) == 7

    def test_exponent_zero_base(self):
        assert exponent(0, 5) == 0