# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
import random
import threading
from collections import defaultdict

from lesson_012.utils import time_track


class Volatility(threading.Thread):

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.files_list = []
        self.result_list = list()

    def run(self):
        data = self.read_file()

        for secid, prices in data.items():
            prices = [float(x) for x in prices]
            min_price = min(prices)
            max_price = max(prices)
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100
            self.result_list = [secid, volatility]

    def read_file(self):
        with open(self.path, mode='r') as current_file:
            next(current_file)
            data = defaultdict(list)

            for line in current_file:
                line = line[:-1]
                line = line.split(',')

                data[line[0]].append(line[2])
            return data


def sort(dict):
    list_tuple_nonzero = []
    list_tuple_zero = []

    sorted_list = list(dict.items())
    sorted_list.sort(key=lambda i: i[1])

    for elem in sorted_list:
        if elem[1] < 0.001:
            list_tuple_zero.append(elem)
            continue
        list_tuple_nonzero.append(elem)
    list_tuple_zero.sort(key=lambda i: i[0])

    return list_tuple_nonzero, list_tuple_zero


def print_result(list_nonzero, list_zero):
    print('Максимальная волотильность:')
    for i in range(3):
        elems = list_nonzero[-i - 1]
        print(f'    {elems[0]} - {elems[1]:.2f}')
    print('Минимальная волотильность:')
    for i in range(3):
        elems = list_nonzero[2 - i]
        print(f'    {elems[0]} - {elems[1]:.2f}')
    print('Нулевая волотильность:')
    print('    ', end='')
    for elem in list_zero:
        print(elem[0], end=', ')


@time_track
def main():
    path = 'trades'
    result_dict = dict()

    list_path = [os.path.join(path, file) for file in os.listdir(path)]

    volatilitys = [Volatility(path=path) for path in list_path]

    for volatility in volatilitys:
        volatility.start()

    for volatility in volatilitys:
        volatility.join()

    for volatility in volatilitys:
        result_dict[volatility.result_list[0]] = volatility.result_list[1]

    sorted_nonzero, sorted_zero = sort(result_dict)
    print_result(sorted_nonzero, sorted_zero)


if __name__ == '__main__':
    main()
