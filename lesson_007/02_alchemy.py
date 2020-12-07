# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
from termcolor import cprint


class Water():

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Mud()
        else:
            return None


class Air():

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None


class Fire():

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ground):
            return Lava()
        else:
            return None


class Ground():

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm():

    def __str__(self):
        return 'Шторм'


class Steam():

    def __str__(self):
        return 'Пар'


class Mud():

    def __str__(self):
        return 'Грязь'


class Lightning():

    def __str__(self):
        return 'Молния'


class Dust():

    def __str__(self):
        return 'Пыль'


class Lava():

    def __str__(self):
        return 'Лава'


elements_dict = {
    'Вода': Water(),
    'Воздух': Air(),
    'Огонь': Fire(),
    'Земля': Ground(),
}

cprint('Добро пожаловать в игру Алхимик!', color='green')
cprint('Можно смешивать следующие элементы:', color='green')
for element in elements_dict:
    cprint(element, color='red')

while True:
    element_1 = input('Введите название первого элемента\n')
    element_2 = input('Введите название второго элемента\n')
    element_1 = element_1.capitalize()
    element_2 = element_2.capitalize()
    print(element_1, '+', element_2, '=', elements_dict[element_1] + elements_dict[element_2])

    end_game = input('Сыграть еще?\n')
    if end_game == 'нет':
        break

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
