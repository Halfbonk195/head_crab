# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    """Снежинка"""

    def __init__(self):
        self.length_flake = sd.random_number(10, 100)
        self.x = sd.random_number(50, 1150)
        self.y = 800

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        self.x += sd.random_number(-10, 10)
        self.y -= 10

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length_flake)

    def can_fall(self):
        return self.y > self.length_flake


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()

    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
