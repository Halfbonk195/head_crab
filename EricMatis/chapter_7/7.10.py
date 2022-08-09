responses = {}
answer_no = ['no', 'n', 'нет', 'ytn', 'тщ']

# Установка флага продолжения опроса
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя
    name = input('\nWhat is your name? ')
    response = input('Where would you like to spend your vacation? ')

    # Ответ сохраняется в словаре
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat.lower() in answer_no:
        polling_active = False

# Опрос завершен, вывести результаты
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f'{name.title()} would like to vacation in the {response}.')
