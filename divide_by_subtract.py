def divide_by_subtract(dividend, divisor):
    """
    Делит dividend на divisor с помощью repeated subtraction.
    Возвращает целую часть (integer division).
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    
    if dividend == 0:
        return 0
    
    # Учитываем знак результата
    sign = 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    
    # Работаем с положительными числами
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    return sign * quotient