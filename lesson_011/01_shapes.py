# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1400, 900)


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def shape(start_point, angle, length_shape):
        inner_angle = 360 // n
        for i in range(0, 360, inner_angle):
            vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
            vector.draw()
            start_point = vector.end_point

    return shape


draw_triangle = get_polygon(n=3)
draw_triangle(start_point=sd.get_point(100, 100), angle=13, length_shape=100)

draw_square = get_polygon(n=4)
draw_square(start_point=sd.get_point(200, 200), angle=20, length_shape=100)

draw_pentagon = get_polygon(n=5)
draw_pentagon(start_point=sd.get_point(350, 350), angle=33, length_shape=100)

draw_hexagon = get_polygon(n=6)
draw_hexagon(start_point=sd.get_point(600, 500), angle=44, length_shape=100)

sd.pause()
