from add import *

def multiply_by_add(a: int, b: int) -> int:
    """Умножает два числа через последовательный вызов add()."""
    result = 0
    
    # Работаем с абсолютными значениями для цикла
    abs_a = abs(a)
    abs_b = abs(b)
    
    for _ in range(abs_b):
        result = add(result, abs_a)
        
    # Определяем знак итогового числа
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return - result
        
    return result

