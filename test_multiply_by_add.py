import unittest
# Импортируем add (на будущее) и multiply_by_add (которого еще нет)
from add import add 
from multiply_by_add import multiply_by_add

class TestMultiplyByAdd(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        # Этот вызов вызовет ошибку, так как функции еще нет
        self.assertEqual(multiply_by_add(3, 4), 12)

