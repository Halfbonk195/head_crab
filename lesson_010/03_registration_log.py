# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):

    def __str__(self):
        return 'Поле имени содержит НЕ только буквы'


class NotEmailError(Exception):

    def __str__(self):
        return 'Поле емейл НЕ содержит @ и точку "."'


def data_validation(line):
    """ Проверка данных, полученных из файла """
    try:
        name, mail, age = line.split(' ')
    except ValueError:
        raise ValueError('НЕ присутсвуют все три поля')

    age = int(age)

    if not name.isalpha():
        raise NotNameError()

    if not ('@' in mail and '.' in mail):
        raise NotEmailError()

    if age < 10 or age > 99:
        raise ValueError('Поле возраст НЕ является числом от 10 до 99')


with open('registrations.txt', mode='r', encoding='utf-8') as data:
    with open('registrations_good.log', mode='w', encoding='utf-8') as registrations_good:
        with open('registrations_bad.log', mode='w', encoding='utf-8') as registrations_bad:
            for line in data:
                try:
                    data_validation(line[:-1])
                except NotNameError as exc:
                    registrations_bad.write(f'{line[:-1]} - {exc}\n')
                    continue
                except NotEmailError as exc:
                    registrations_bad.write(f'{line[:-1]} - {exc}\n')
                    continue
                except ValueError as exc:
                    registrations_bad.write(f'{line[:-1]} - {exc}\n')
                    continue

                registrations_good.write(line)
