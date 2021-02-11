# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
from random import randint, choice

from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __str__(self):
        return 'Ошибка бога'


class DrunkError(Exception):

    def __str__(self):
        return 'Жестко напился'


class CarCrashError(Exception):

    def __str__(self):
        return 'Попал в автокатастрофу'


class GluttonyError(Exception):

    def __str__(self):
        return 'Объелся и лопнул'


class DepressionError(Exception):

    def __str__(self):
        return 'Впал в депрессию'


class SuicideError(Exception):

    def __str__(self):
        return 'Покончил жизнь самоубийством'


_list_of_exceptions = [IamGodError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError(), SuicideError()]


def one_day():
    carma = randint(1, 7)
    random_number = randint(1, 13)
    if random_number == 1:
        raise choice(_list_of_exceptions)
    return carma


sum_carma = 0
day = 0
while True:
    day += 1
    cprint(f'------------День {day}------------', color='green')
    try:
        sum_carma += one_day()
        print(f'Количество кармы {sum_carma}')
    except Exception as exc:
        cprint(f'Произошло: {exc}', color='red')
        with open('log.txt', 'a', encoding='utf-8') as ff:
            ff.write(f'День {day:<5} {exc}\n')

    if sum_carma >= ENLIGHTENMENT_CARMA_LEVEL:
        break

# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


# https://goo.gl/JnsDqu
