""" движок для игры "быки и коровы" """
from random import randint

_holder_number = []
_result = {}
_positive_answer = ['да', 'Да', 'yes', 'Yes', 'Ага', 'ага', 'lf', 'Lf', 'fuf', 'Fuf']
_want_rules = ['Правила', 'правила']
_surrender = ['Сдаюсь', 'Все', 'Я слабак', 'я слабак', 'нет', 'Нет', 'Неа', 'неа', 'no', 'No']


def answers(response):
    if response in _positive_answer:
        return 'game'
    elif response in _want_rules:
        return 'rules'
    elif response in _surrender:
        print('Число то было простое:', _holder_number)
        return 'game over'
    else:
        return None


def take_rules():
    print('Правила игры "Быки и коровы":')
    print('Компьютер загадывает четырехзначное число, все цифры которого различны '
          '(первая цифра числа отлична от нуля).\nИгроку необходимо разгадать задуманное число.\nИгрок вводит '
          'четырехзначное число c неповторяющимися цифрами, компьютер сообщают о количестве «быков» и «коров» в '
          'названном числе\n«бык» — цифра есть в записи задуманного числа и стоит в той же позиции, что и в '
          'задуманном числе\n«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции, '
          'что и в задуманном числе')
    print('Например, если задумано число 3275 и названо число 1234, получаем в названном числе одного «быка» и '
          'одну «корову».\nЧисло отгадано в том случае, если имеем 4 «быка».')


def guess_number():
    global _holder_number

    _holder_number.append(randint(1, 9))
    for i in range(1, 4):
        _holder_number.append(randint(0, 9))


def check_number(number_str):
    global _result
    _result = {'bulls': 0, 'cows': 0}
    if len(set(number_str)) == len(number_str) and int(number_str[0]) != 0:
        if number_str.isnumeric() and len(number_str) == 4:
            for estimated_number in number_str:
                for guessed_number in _holder_number:
                    numbers_equal = int(estimated_number) == guessed_number
                    numbers_in_same_positions = number_str.index(estimated_number) == _holder_number.index(guessed_number)
                    if numbers_equal and numbers_in_same_positions:
                        _result['bulls'] += 1
                    elif numbers_equal:
                        _result['cows'] += 1
            return _result

        else:
            return False
    else:
        return False


def is_gameover():
    return _result['bulls'] == 4
