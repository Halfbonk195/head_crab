# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point, 5)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


