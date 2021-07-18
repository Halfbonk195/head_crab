# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def log_errors(name):
    def log_errors_inner(func):
        def surrogate(*args, **kwargs):
            result = None
            massage_2 = str()
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                file = open(name, 'a', encoding='utf8')
                massage_1 = func.__name__
                for elem in args:
                    massage_2 += str(elem)
                for elem, item in kwargs.items():
                    if massage_2:
                        massage_2 += ', '
                    massage_2 += elem + '=' + str(item)
                massage_2 = '(' + massage_2 + ')'
                massage_3 = str(type(exc))
                massage_4 = str(exc)

                file.write(massage_1 + massage_2 + ' ' + massage_3 + ' ' + massage_4)
                file.write('\n')
                raise Exception(exc)

            return result

        return surrogate

    return log_errors_inner


# Проверить работу на следующих функциях
@log_errors('function_errors.log')
def perky(x, param):
    return param / 0


@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

try:
    perky(54, param=42)
except Exception as exc:
    print(f'Invalid format: {exc}')

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
