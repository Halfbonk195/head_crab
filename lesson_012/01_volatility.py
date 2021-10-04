# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import os
from collections import defaultdict


class Volatility:

    def __init__(self, path, list_tuple_nonzero, list_tuple_zero):
        self.path = path
        self.files_list = []
        self.result_dict = dict()
        self.list_tuple_nonzero = list_tuple_nonzero
        self.list_tuple_zero = list_tuple_zero

    def run(self):
        for file in os.listdir(self.path):
            norm_path = os.path.join(self.path, file)
            data = self.read_file(norm_path)

            for secid, prices in data.items():
                prices = [float(x) for x in prices]
                min_price = min(prices)
                max_price = max(prices)
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100
                self.result_dict[secid] = volatility
        self.sort()

    def sort(self):
        sorted_list = list(self.result_dict.items())
        sorted_list.sort(key=lambda i: i[1])

        for elem in sorted_list:
            if elem[1] < 0.001:
                self.list_tuple_zero.append(elem)
                continue
            self.list_tuple_nonzero.append(elem)
        sorted_list_zero.sort(key=lambda i: i[0])

    def read_file(self, path):
        with open(path, mode='r') as current_file:
            next(current_file)
            data = defaultdict(list)

            for line in current_file:
                line = line[:-1]
                line = line.split(',')

                data[line[0]].append(line[2])
            return data


def print_result():
    print('Максимальная волотильность:')
    for i in range(3):
        elems = sorted_list_nonzero[-i - 1]
        print(f'    {elems[0]} - {elems[1]:.2f}')
    print('Минимальная волотильность:')
    for i in range(3):
        elems = sorted_list_nonzero[2 - i]
        print(f'    {elems[0]} - {elems[1]:.2f}')
    print('Нулевая волотильность:')
    for elem in sorted_list_zero:
        print(elem[0], end=', ')


path = 'trades'
sorted_list_nonzero = []
sorted_list_zero = []
volatility_class = Volatility(path=path, list_tuple_nonzero=sorted_list_nonzero, list_tuple_zero=sorted_list_zero)
volatility_class.run()
print_result()
