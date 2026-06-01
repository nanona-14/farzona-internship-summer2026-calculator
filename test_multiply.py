import unittest
# Импортируем вашу функцию из файла (предполагаем, что ваш файл называется multiply.py)
from multiply import multiply 

class TestMultiply(unittest.TestCase):

    # 1. Проверяем работу с целыми и дробными числами
    def test_multiply_valid_numbers(self):
        self.assertEqual(multiply(3, 4), 12)       # Целые числа
        self.assertEqual(multiply(2.5, 2), 5.0)    # Дробные числа
        self.assertEqual(multiply(-2, 3), -6)      # Отрицательные числа

    # 2. Проверяем защиту от не-числовых данных (строки, списки)
    def test_multiply_rejects_non_numeric(self):
        with self.assertRaises(TypeError):
            multiply("3", 4)  # Строка вместо числа должна вызывать ошибку
        with self.assertRaises(TypeError):
            multiply(5, [1, 2]) # Список вместо числа
