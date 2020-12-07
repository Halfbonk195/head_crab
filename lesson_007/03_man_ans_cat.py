# -*- coding: utf-8 -*-

from random import randint, choice
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def pick_up_cat(self, cat):
        cat.house = self.house
        cprint('{} подобрал котика {}'.format(self.name, cat.name), color='cyan')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play_games(self):
        cprint('{} играл в компьютерные игры целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.fullness -= 5

    def shopping_cat(self):
        if self.house.money >= 60:
            self.house.money -= 60
            self.house.cat_food += 60
            self.fullness -= 10
            cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
        else:
            self.fullness -= 5
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def clean_house(self):
        self.house.cat_mud -= 100
        self.fullness -= 20
        cprint('{} прибрался в доме'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 20:
            self.shopping_cat()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_mud > 100 and self.fullness > 20:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_games()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Я котик {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('котик {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет кошачей еды'.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        self.fullness -= 10
        cprint('Котик {} спит'.format(self.name), color='yellow')

    def tear_wallpaper(self):
        if self.name == 'Вуглусрат':
            self.house.cat_mud += 50
            cprint('Котик {} обосрал все углы в доме!!!'.format(self.name), color='green')
        else:
            self.house.cat_mud += 5
            cprint('Котик {} дерет обои'.format(self.name), color='yellow')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('Котик {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 60
        self.cat_food = 0
        self.cat_mud = 0
        self.money = 60

    def __str__(self):
        return 'В доме еды осталось {}, кошачей еды осталось {}, денег осталось {}, грязи {}'.format(
            self.food, self.cat_food, self.money, self.cat_mud)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cats = [
    Cat(name='Барсик'),
    Cat(name='Вуглусрат'),
    Cat(name='Борис'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
for cat in cats:
    rand_citizen = choice(citizens)
    rand_citizen.pick_up_cat(cat=cat)

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
