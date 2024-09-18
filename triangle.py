
def classify_triangle(input_string: str) -> str:
    # Разделяем входную строку на три стороны и преобразуем их в числа
    a, b, c = map(float, input_string.split())

    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Не существует"

    # Полупериметр
    p = (a + b + c) / 2

    # Площадь по формуле Герона
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    # Возврат площади, округленной до двух знаков после запятой
    return f"{area:.2f}"


# Чтение входных данных
input_string = input()
result = classify_triangle(input_string)
print(result)