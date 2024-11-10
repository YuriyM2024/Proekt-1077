def create_actor(**kwargs):
    base_actor = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 47,
    }

    # Обновляем базовый словарь новыми значениями из kwargs
    base_actor.update(kwargs)

    return base_actor


# Sample Input 1:
actor = create_actor()
print(actor)


# Sample Input 2:
actor = create_actor(height=190, movies=['Дедпул', 'Главный герой'])
print(actor)

# Sample Input 3:

actor = create_actor(name='Jack', age=20,    surname='Qwerty')
print(actor)

# Sample Input 4:

actor = create_actor(surname='Уиллис', age=69, name='Брюс')
print(actor)
