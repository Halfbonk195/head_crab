# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cat_food = 30

    def __str__(self):
        return 'В холодильнике {} едениц человеческой еды, {} едениц кошачей еды, количество денег в тумбочке' \
               ' - {} едениц, дом грязный на {} пунктов'.format(self.food, self.cat_food, self.money, self.mud)


class Human:
    count_food = 0

    def __init__(self, name, home, cat_number):
        self.name = name
        self.home = home
        self.fullness = 30
        self.happiness = 100
        self.count_cats = cat_number
        self.alive = True
        Human.count_food = 0

    def __str__(self):
        return '{} счастья {}, сытость {}'.format(self.name, self.happiness, self.fullness)

    def eat(self):
        eat_food = randint(15, 30)

        if self.home.food < eat_food:
            if self.home.food > 0:
                eat_food = self.home.food
            else:
                # print('{} - еда закончилась!'.format(self.name))
                self.fullness -= 10
                return
        self.home.food -= eat_food
        self.fullness += eat_food
        Human.count_food += eat_food
        self.happiness += 2
        ending = 'а' if isinstance(self, Wife) else ''
        # print('{} поел{} {} еды'.format(self.name, ending, eat_food))

    def pet_cat(self):
        dice = randint(1, 3)
        if dice == 1:
            self.happiness += 5
            ending = 'а' if isinstance(self, Wife) else ''
            # cprint('{} погладил{} кота'.format(self.name, ending), color='green')
        else:
            return


class Husband(Human):
    count_money = 0

    def __init__(self, name, home, salary, cat_number):
        self.salary = salary
        Husband.count_money = 0
        super().__init__(name=name, home=home, cat_number=cat_number)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            if self.alive:
                # cprint('{} умер от голода...'.format(self.name), color='red')
                self.alive = False
            return
        if self.happiness < 10:
            if self.alive:
                # cprint('{} умер от депресии...'.format(self.name), color='red')
                self.alive = False
            return
        self.pet_cat()

        if self.home.mud > 90:
            self.happiness -= 10

        dice = randint(1, 5)
        if self.fullness <= 15:
            self.eat()
        elif self.home.money < 200:
            self.work()
        elif self.happiness <= 20:
            self.gaming()
        elif dice == 1 or dice == 2:
            self.work()
        elif dice == 3:
            self.eat()
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        self.happiness -= 3
        self.home.money += self.salary
        Husband.count_money += self.salary
        # print('{} сходил на работу'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        if self.happiness <= 80:
            self.happiness += 20
        else:
            self.happiness = 100
        # print('{} весь день играл в WoT'.format(self.name))


class Wife(Human):
    fur_coat = 0

    def __init__(self, name, home, cat_number):
        Wife.fur_coat = 0
        super().__init__(name=name, home=home, cat_number=cat_number)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            if self.alive:
                # cprint('{} умерла от голода...'.format(self.name), color='red')
                self.alive = False
            return
        if self.happiness < 10:
            if self.alive:
                # cprint('{} умерла от депресии...'.format(self.name), color='red')
                self.alive = False
            return
        self.pet_cat()

        if self.home.mud > 90:
            self.happiness -= 10
        dice = randint(1, 30)
        if self.fullness <= 15:
            self.eat()
        elif self.home.food < 60 or self.home.cat_food < 20 * (self.count_cats - Cat.cat_die):
            self.shopping()
        elif self.home.mud > 200:
            self.clean_house()
        elif self.happiness < 20:
            self.buy_fur_coat()
        elif 1 <= dice < 8:
            self.eat()
        elif 8 <= dice < 18:
            self.shopping()
        elif 18 <= dice < 29:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def shopping(self):
        self.fullness -= 10
        buy_food = randint(30, 100) if self.home.food < 1000 else 5
        buy_food_cat = 30 * (self.count_cats - Cat.cat_die) if self.home.cat_food <= 30 * (
                    self.count_cats - Cat.cat_die) else 0

        if self.home.money < buy_food + buy_food_cat:
            # print('{} денег не хватает купить еду!'.format(self.name))
            return
        self.home.food += buy_food
        self.home.cat_food += buy_food_cat
        self.home.money -= buy_food + buy_food_cat
        # print('{} сходила в магазин и купила {} едениц еды для людей и {} едениц для котов'.format(self.name, buy_food,
        #                                                                                            buy_food_cat))

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.home.money < 350:
            # print('{} хотела купить шубу, но денег не хватило!'.format(self.name))
            return
        self.home.money -= 350
        Wife.fur_coat += 1
        if self.happiness <= 40:
            self.happiness += 60
        else:
            self.happiness = 100
        # print('{} купила себе шубу!'.format(self.name))

    def clean_house(self):
        self.fullness -= 10
        self.happiness -= 2
        cleaning = randint(10, 100)
        if self.home.mud < cleaning:
            self.home.mud = 0
        else:
            self.home.mud -= cleaning
        # print('{} прибралась дома'.format(self.name))


class Child(Human):

    def __init__(self, name, home, cat_number):
        super().__init__(name=name, home=home, cat_number=cat_number)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            # cprint('Ребенок {} умер от голода, вы изверги!!!'.format(self.name), color='red')
            return

        dice = randint(1, 2)
        if self.fullness <= 15:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        eat_food = randint(2, 10)
        if self.home.food < eat_food:
            # cprint('{} - еда закончилась!'.format(self.name), color='blue')
            self.fullness -= 10
            return
        self.home.food -= eat_food
        self.fullness += eat_food
        Human.count_food += eat_food
        # cprint('Ребенок {} поел {} еды'.format(self.name, eat_food), color='blue')

    def sleep(self):
        self.fullness -= 10
        # cprint('Ребенок {} проспал весь день'.format(self.name), color='blue')


class Cat:
    cat_die = 0

    def __init__(self, name, home):
        self.name = name
        self.fullness = 30
        self.home = home
        self.cat_alive = True
        Cat.cat_die = 0

    def __str__(self):
        return 'Котик по имени {}, сытость - {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            if self.cat_alive:
                # cprint('Котик {} умер от голода! Чтож вы за люди...'.format(self.name), color='red')
                Cat.cat_die += 1
                self.cat_alive = False
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        eat_food = randint(5, 10)
        if self.home.cat_food < eat_food:
            if self.home.cat_food > 0:
                eat_food = self.home.cat_food
            else:
                # cprint('У котика по имени {} закончилась еда!'.format(self.name), color='yellow')
                self.fullness -= 10
                return
        self.home.cat_food -= eat_food
        self.fullness += 2 * eat_food
        # cprint('Котик {} поел еды {} едениц'.format(self.name, eat_food), color='yellow')

    def sleep(self):
        self.fullness -= 10
        # cprint('Котик {} весь день спал'.format(self.name), color='yellow')

    def soil(self):
        self.fullness -= 10
        self.home.mud += 5
        # cprint('Котик {} весь день драл обои'.format(self.name), color='yellow')


class Simulation:

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents

    def experiment(self, salary):
        number_cats = 5
        my_home = House()
        serge = Husband(name='Сережа', home=my_home, salary=salary, cat_number=number_cats)
        masha = Wife(name='Маша', home=my_home, cat_number=number_cats)
        kolya = Child(name='Коля', home=my_home, cat_number=number_cats)
        my_cat_list = []
        cat_name_list = ['Барсик', 'Кузя', 'Рыся', 'Кыся', 'Муся', 'Пуся', 'Бусинка', 'Леопольд', 'Вуглусрат', 'Йогурт',
                         'Кактус', 'Лапусичка', 'Крош', 'Сема']

        for number in range(1, number_cats + 1):
            name_cat = choice(cat_name_list)
            my_cat_list.append(Cat(name=name_cat, home=my_home))

        for day in range(364):
            # cprint('================== День {} =================='.format(day), color='red')
            dice_money = randint(1, 365)
            if 0 < dice_money <= self.money_incidents:
                my_home.money -= my_home.money // 2
                print('------------------Пропали деньги на {} день!------------------'.format(day))
            dice_food = randint(1, 365)
            if 0 < dice_food <= self.food_incidents:
                my_home.food -= my_home.food // 2
                print('------------------Пропала еда на {} день!------------------'.format(day))

            my_home.mud += 5
            serge.act()
            masha.act()
            kolya.act()
            for cat in my_cat_list:
                cat.act()
            # cprint(serge, color='cyan')
            # cprint(masha, color='cyan')
            # cprint(kolya, color='cyan')
            # for cat in my_cat_list:
            #     cprint(cat, color='cyan')
            # cprint(my_home, color='cyan')
        print('Еды съедено - {}, шуб куплено - {}, денег заработано - {}'.format(Human.count_food, Wife.fur_coat,
                                                                                 Husband.count_money))
        print('Серега жив {}, Маша жива {}, Коля жив {}'.format(serge.alive, masha.alive, kolya.alive))
        return number_cats - Cat.cat_die


######################################################## Часть третья
#
# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов

for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)

            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
            print('Вероятность пропажи денег {}, пропажи еды - {}'.format(money_incidents, food_incidents))
            print()
