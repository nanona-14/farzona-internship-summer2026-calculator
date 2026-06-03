import unittest
# Импортируем вашу функцию из файла (предполагаем, что ваш файл называется add.py)
from add import add 

class TestAdd(unittest.TestCase):

    # 1. Проверяем работу с целыми и дробными числами
    def test_add_valid_numbers(self):
        self.assertEqual(add(3, 4), 7)         # Целые числа
        self.assertEqual(add(2.5, 2), 4.5)     # Дробные числа
        self.assertEqual(add(-2, 3), 1)        # Отрицательные числа

    # 2. Проверяем защиту от не-числовых данных (строки, списки)
    def test_add_rejects_non_numeric(self):
        with self.assertRaises(TypeError):
            add("3", 4)  # Строка вместо числа должна вызывать ошибку
        with self.assertRaises(TypeError):
            add(5, [1, 2]) # Список вместо числа
