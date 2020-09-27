# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
# point = sd.get_point(300, 300)

# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном


def triangle(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.random_color())

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=sd.random_color())

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=sd.random_color())


point_0 = sd.get_point(300, 300)
length_triangle = 200
for angle in range(0, 361, 20):
    triangle(point=point_0, angle=angle, length=length_triangle)

# triangle(point=point_0, angle=angle, length=length_triangle)
# for length_triangle in range(10, 200, 30):
#     point_0.x -= 15
#     point_0.y -= 10
#     triangle(point=point_0, angle=0, length=length_triangle)

sd.pause()

