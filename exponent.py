def exponent(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return result