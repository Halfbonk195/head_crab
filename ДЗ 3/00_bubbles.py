# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1900, 1000)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step, width, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=width, color=color)

# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 5)

for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    width = random.randint(2, 5)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    bubble(point, step, width, color)
sd.pause()
