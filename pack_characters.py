def pack_characters(input_string):
    # Разбиваем строку на символы
    characters = input_string.split()

    # Список для хранения подсписков
    result = []

    # Переменная для текущего подсписка
    current_group = []

    for char in characters:
        if not current_group or current_group[-1] == char:
            # Если текущая группа пуста или последний элемент равен текущему символу
            current_group.append(char)
        else:
            # Если символ отличается, добавляем текущую группу в результат
            result.append(current_group)
            # Начинаем новую группу
            current_group = [char]

    # Добавляем последнюю группу в результат
    if current_group:
        result.append(current_group)

    return result


# Ввод строки
input_string = input()
# Получаем результат
output = pack_characters(input_string)
# Выводим результат
print(output)
