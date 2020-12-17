# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class StatsLetters():

    def __init__(self, f_name):
        self.collector = {}
        self.sorted_collection = []
        self.quantity = 0
        self.f_name = f_name

    def do_all_methods(self):
        self.collect()
        self.sort()
        self.output()

    def collect(self):
        with open(self.f_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.collector:
                            self.collector[char] += 1
                        else:
                            self.collector[char] = 1
                    else:
                        continue

    def sort(self):
        pass

    def output(self):
        print(f'+{"-" * 9}+{"-" * 9}+')
        print(f'|{"Буква":^9}|{"Частота":^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')

        for element in self.sorted_collection:
            frequency = element[0]
            char = element[1]
            self.quantity += frequency
            print(f'|{char:^9}|{frequency:^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')

        print(f'|{"Итого:":^9}|{self.quantity:^9}|')
        print(f'+{"-" * 9}+{"-" * 9}+')


class Frequency(StatsLetters):

    def sort(self):
        for key, value in self.collector.items():
            self.sorted_collection.append([value, key])
        self.sorted_collection.sort(reverse=True)


class AlphabetIncrease(StatsLetters):

    def sort(self):
        for key, value in self.collector.items():
            self.sorted_collection.append([key, value])
        self.sorted_collection.sort()
        tmp_collection = []
        for key, value in self.sorted_collection:
            tmp_collection.append([value, key])
        self.sorted_collection = tmp_collection


class AlphabetDecrease(StatsLetters):

    def sort(self):
        for key, value in self.collector.items():
            self.sorted_collection.append([key, value])
        self.sorted_collection.sort(reverse=True)
        tmp_collection = []
        for key, value in self.sorted_collection:
            tmp_collection.append([value, key])
        self.sorted_collection = tmp_collection


file_name = 'voyna-i-mir.txt'

stat_1 = Frequency(f_name=file_name)
stat_2 = AlphabetIncrease(f_name=file_name)
stat_3 = AlphabetDecrease(f_name=file_name)
stat_1.do_all_methods()
stat_2.do_all_methods()
stat_3.do_all_methods()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
