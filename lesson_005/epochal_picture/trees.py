# -*- coding: utf-8 -*-
"""
    Модуль отрисовки дерева (фрактал) v1.0
"""

import simple_draw as sd

def branch_draw(point, angle, length):
    color = sd.COLOR_DARK_ORANGE
    if length < 3:
        return
    if 100 <= length < 150:
        width = 8
    elif 50 <= length < 100:
        width = 5
    elif 15 < length < 50:
        width = 3

    elif length < 15:
        width = 1
        color = sd.COLOR_GREEN
    else:
        width = 6

    step_angle = 25 + sd.random_number(-10, 10)
    v1 = sd.get_vector(start_point=point, angle=angle - step_angle, length=length, width=width)
    v1.draw(color)
    v2 = sd.get_vector(start_point=point, angle=angle + step_angle, length=length, width=width)
    v2.draw(color)
    length *= (1 + sd.random_number(-10, 10) / 100) * 0.74
    branch_draw(point=v1.end_point, angle=angle - step_angle, length=length)
    branch_draw(point=v2.end_point, angle=angle + step_angle, length=length)


def get_tree(point, length, angle=90):
    if 100 <= length:
        width = 9
    elif 70 <= length < 100:
        width = 8
    elif 20 <= length < 70:
        width = 5
    elif length < 20:
        width = 4
    sd.get_vector(start_point=point, angle=angle, length=length, width=width).draw(color=sd.COLOR_DARK_ORANGE)
    point = sd.get_point(point.x, point.y + length)
    branch_draw(point=point, angle=angle, length=length/1.3)




