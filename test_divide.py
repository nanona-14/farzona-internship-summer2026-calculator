import unittest
from divide import divide

class TestDivide(unittest.TestCase):
    
    def test_normal_division(self):
        """Тест обычного деления положительных чисел"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_negative_numbers(self):
        """Тест деления с отрицательными числами"""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_float_division(self):
        """Тест деления, результатом которого является дробь"""
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Тест, что деление на ноль вызывает ошибку ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

# if __name__ == '__main__':
#     unittest.main()
