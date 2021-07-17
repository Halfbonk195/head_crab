# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import time


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


_n = 10000


def polynom(poly):
    ylop = 0
    i = poly
    while i >= 1:
        ylop = ylop * 10 + i % 10
        i = i // 10

    if poly == ylop:
        return poly
    else:
        return None


def lucky_number(num):
    if num < 10:
        return num

    list_for_numbers = []

    for elem in str(num):
        list_for_numbers.append(int(elem))

    lenth_of_number = len(list_for_numbers)

    n = lenth_of_number // 2
    sum_1, sum_2 = 0, 0

    for i in range(0, n):
        sum_1 += list_for_numbers[i]

    if lenth_of_number % 2:
        for i in range(n + 1, lenth_of_number):
            sum_2 += list_for_numbers[i]
    else:
        for i in range(n, lenth_of_number):
            sum_2 += list_for_numbers[i]

    if sum_1 == sum_2:
        return num
    else:
        return None


class PrimeNumbers:
    """Итератор последовательности простых чисел количеством N"""

    def __init__(self, n):
        self.i = 0
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 0
        # self.prime_numbers = []
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()

            for number in range(self.i, self.i + 1):
                for prime in self.prime_numbers:
                    if number % prime == 0:
                        break
                else:
                    self.prime_numbers.append(number)
                    return number


prime_number_iterator = PrimeNumbers(n=_n)
for number in prime_number_iterator:
    if number is not None:
        print(number)

result_poly = filter(polynom, prime_number_iterator.prime_numbers)
print(f'Список полиндромов для n = {_n}:')
print(list(result_poly))

result_lucky = filter(lucky_number, prime_number_iterator.prime_numbers)
print(f'Список счастливых чисел для n = {_n}:')
print(list(result_lucky))


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик
def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for number in prime_numbers_generator(n=_n):
    print(number)

result_poly = filter(polynom, prime_numbers_generator(n=_n))
print(f'Список полиндромов для n = {_n}:')
print(list(result_poly))

result_lucky = filter(lucky_number, prime_numbers_generator(n=_n))
print(f'Список счастливых чисел для n = {_n}:')
print(list(result_lucky))

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
