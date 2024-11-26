def chunked(input_list, n):
    # Создаем список для хранения чанков
    chunks = []

    # Проходим по элементам списка с шагом n
    for i in range(0, len(input_list), n):
        # Добавляем подсписок длиной n в список чанков
        chunks.append(input_list[i:i + n])

    return chunks


# Ввод символов
input_string = input()
# Ввод числа n
n = int(input())

# Преобразуем строку в список символов
input_list = input_string.split()

# Вызываем функцию chunked и выводим результат
output = chunked(input_list, n)
print(output)