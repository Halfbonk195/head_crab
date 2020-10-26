# -*- coding: utf-8 -*-
"""
    Модуль для рисования правильных многоугольников
"""
import simple_draw as sd
import math


def triangle(start_point, length_shape, angle=0, width=3, hight=0, color=sd.COLOR_YELLOW):
    """
        Отрисовывает равносторонний треугольник если hight = 0
        Отрисовывает треугольник высотой hight, если hight != 0
    """
    if hight:
        slope_length = ((length_shape / 2) ** 2 + hight ** 2) ** .5
        alpha = math.asin(length_shape / (2 * slope_length)) * 180 / math.pi
        vector1 = sd.get_vector(start_point=start_point, angle=angle, length=length_shape, width=width)
        vector2 = sd.get_vector(start_point=vector1.end_point, angle=angle+90+alpha, length=slope_length, width=width)
        vector3 = sd.get_vector(start_point=vector2.end_point, angle=angle+270-alpha, length=slope_length, width=width)
        vector1.draw(color)
        vector2.draw(color)
        vector3.draw(color)
    else:
        draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=120, width=width)


def square(start_point, length_shape, angle=0, width=3):
    """
        Отрисовывает квадрат
        :param start_point, angle, length_shape
    """
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=90, width=width)


def pentagon(start_point, length_shape, angle=0, width = 3):
    """
        Отрисовывает 5-ти угольник
        :param start_point, angle, length_shape
    """
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=72, width=width)


def hexagon(start_point, length_shape, angle=0, width = 3):
    """
        Отрисовывает 6-ти угольник
        :param start_point, angle, length_shape
    """
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=60, width=width)


def draw_vector(start_point, angle, length_shape, inner_angle, width):
    for i in range(0, 360, inner_angle):
        vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=width)
        vector.draw()
        start_point = vector.end_point
