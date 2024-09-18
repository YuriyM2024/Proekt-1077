import re


def count_unique_words(text: str) -> int:
    # Используем регулярное выражение для нахождения всех слов
    words = re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text)

    # Приводим все слова к нижнему регистру и помещаем в множество для подсчета уникальных
    unique_words = set(word.lower() for word in words)

    # Возвращаем количество уникальных слов
    return len(unique_words)


# Чтение входных данных
input_text = input()
result = count_unique_words(input_text)
print(result)