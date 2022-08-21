from random import randint


class Die:
    """Создает sides-гранный кубик"""

    def __init__(self, sides=6):
        self.sides = sides

    def __str__(self):
        return f'{self.sides}-гранный кубик'

    def roll_die(self):
        print(f'{randint(1, self.sides)}')


def die_func(my_die_class, number_try):
    print(f'Бросаем {my_die_class}')
    for n in range(1, number_try + 1):
        my_die_class.roll_die()
    print()


die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

die_func(die_6, 10)
die_func(die_10, 10)
die_func(die_20, 10)
