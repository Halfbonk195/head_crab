# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 77


def one_day():
    carma = randint(1, 7)
    return carma


sum_carma = 0
day = 0
while True:
    day += 1
    sum_carma += one_day()
    print(f'День {day}, количество кармы {sum_carma}')
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

7

# TODO здесь ваш код

# https://goo.gl/JnsDqu
