def process(input_string: str) -> str:
    # Разбиваем входную строку на список чисел и конвертируем их в целые числа
    numbers = list(map(int, input_string.split()))
    
    # Инициализируем счетчики
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    # Обходим все числа и подсчитываем их количество по категориям
    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
            
    # Форматируем и возвращаем результат
    return f"выше нуля: {positive_count}, ниже нуля: {negative_count}, равна нулю: {zero_count}"

# Чтение входной строки
input_string = input()
output_string = process(input_string)
print(output_string)
