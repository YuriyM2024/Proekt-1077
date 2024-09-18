def check_all_students_passed(scores_input, names_input):
    # Преобразуем входные строки в списки целых чисел и имен
    scores = list(map(int, scores_input.split(',')))
    names = names_input.split(',')

    # Список для хранения имён студентов, не сдавших
    failed_students = []

    # Проверяем каждый балл
    for score, name in zip(scores, names):
        if score < 35:
            failed_students.append(name.strip())  # Добавляем имя в список не сдавших

    # Если список не сдавших пустой, значит все сдали
    if not failed_students:
        return "Все сдали"
    else:
        # Формируем результат для студентов, не сдавших
        result = "Есть не сдавшие"
        return result, failed_students


# Чтение входных данных
scores_input = input()
names_input = input()

result = check_all_students_passed(scores_input, names_input)

# Обрабатываем вывод в зависимости от результата
if isinstance(result, tuple):
    print(result[0])
    for name in result[1]:
        print(name)
else:
    print(result)
