def modulo(dividend, divisor):
    """
    Возвращает остаток от деления dividend на divisor,
    используя только операцию вычитания.
    """
    if divisor == 0:
        raise ValueError("Modulo by zero is not allowed")
    
    if dividend == 0:
        return 0
    
    # Учитываем знак (в Python остаток имеет знак делителя)
    sign = 1 if divisor > 0 else -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    # Вычитаем divisor, пока можем
    while dividend >= divisor:
        dividend -= divisor
    
    return sign * dividend