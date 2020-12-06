# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    """Снежинка"""

    def __init__(self, y=0):
        self.length_flake = sd.random_number(50, 100)
        self.x = sd.random_number(50, 1150)
        self.y = sd.random_number(y, 800)

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        self.x += sd.random_number(-5, 10)
        self.y -= sd.random_number(5, 10)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length_flake)

    def can_fall(self):
        return self.y > self.length_flake


def get_flakes(count):
    snowflakes_list = []
    for _ in range(0, count):
        snowflakes_list.append(Snowflake())
    return snowflakes_list


def get_fallen_flakes(flakes):
    fallen_flakes = []
    for flake in flakes:
        if not flake.can_fall():
            fallen_flakes.append(flake)
    return fallen_flakes

def append_flakes(count):
    for flake in count:
        flake.__init__(y=sd.resolution[1])

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
N = 20
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    flakes[0].clear_previous_picture()
    for flake in flakes:
        flake.move()
        flake.draw()

    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
         append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
