def multiply(a, b):
    # Добавляем валидацию типов (разрешаем только целые int и дробные float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами (int или float)")
        
    return a * b
