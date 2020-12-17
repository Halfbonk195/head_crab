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
from pprint import pprint

file_name = 'voyna-i-mir.txt'

collector = {}
with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char.isalpha():
                if char in collector:
                    collector[char] += 1
                else:
                    collector[char] = 1
            else:
                continue

sorted_collection = []

for key, value in collector.items():
    sorted_collection.append([value, key])
sorted_collection.sort(reverse=True)

print(f'+{"-" * 9}+{"-" * 9}+')
print(f'|{"Буква":^9}|{"Частота":^9}|')
print(f'+{"-" * 9}+{"-" * 9}+')

quantity = 0
for element in sorted_collection:
    frequency = element[0]
    char = element[1]
    quantity += frequency
    print(f'|{char:^9}|{frequency:^9}|')
print(f'+{"-" * 9}+{"-" * 9}+')

print(f'|{"Итого:":^9}|{quantity:^9}|')
print(f'+{"-" * 9}+{"-" * 9}+')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
