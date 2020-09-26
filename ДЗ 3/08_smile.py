# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (1400, 800)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    # Рисуем эллипс
    left_bottom, right_top = sd.get_point(x, y), sd.get_point(x + 190, y + 160)
    sd.ellipse(left_bottom, right_top, color, 2)
    # Рисуем глазки
    sd.circle(sd.get_point(x + 55, y + 100), 9, color, 2)
    sd.circle(sd.get_point(x + 125, y + 100), 9, color, 2)
    # Рисуем рот
    sd.line(sd.get_point(x + 60, y + 50), sd.get_point(x + 120, y + 50), color, 2)
    sd.line(sd.get_point(x + 60, y + 50), sd.get_point(x + 60, y + 40), color, 2)
    sd.line(sd.get_point(x + 120, y + 50), sd.get_point(x + 120, y + 40), color, 2)
    # Рисуем нос
    sd.line(sd.get_point(x + 90, y + 110), sd.get_point(x + 70, y + 70), color, 2)
    sd.line(sd.get_point(x + 70, y + 70), sd.get_point(x + 90, y + 70), color, 2)
    # Рисуем ушки
    sd.line(sd.get_point(x + 20, y + 130), sd.get_point(x + 50, y + 190), color, 2)
    sd.line(sd.get_point(x + 50, y + 190), sd.get_point(x + 70, y + 155), color, 2)
    sd.line(sd.get_point(x + 168, y + 130), sd.get_point(x + 140, y + 190), color, 2)
    sd.line(sd.get_point(x + 140, y + 190), sd.get_point(x + 120, y + 155), color, 2)

for i in range(10):
    point_x = random.randint(0, sd.resolution[0] - 180)
    point_y = random.randint(0, sd.resolution[1] - 160)
    point = sd.get_point(point_x, point_y)
    smile(point.x, point.y, sd.random_color())

sd.pause()
