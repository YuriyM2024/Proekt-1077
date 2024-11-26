def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def pascal(n):
    row = []
    for k in range(n + 1):
        # Вычисляем биномиальный коэффициент C(n, k)
        coefficient = factorial(n) // (factorial(k) * factorial(n - k))
        row.append(coefficient)
    return row

# Считываем входные данные
n = int(input())

# Получаем и выводим строку
result = pascal(n)
print(result)