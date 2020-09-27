# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1400, 900)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(start_point, angle, length_shape):
#     for i in range(0, 361, 120):
#         vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
#         vector.draw()
#         start_point = vector.end_point
#
#
# def square(start_point, angle, length_shape):
#     for i in range(0, 361, 90):
#         vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
#         vector.draw()
#         start_point = vector.end_point
#
#
# def pentagon(start_point, angle, length_shape):
#     for i in range(0, 361, 72):
#         vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
#         vector.draw()
#         start_point = vector.end_point
#
#
# def hexagon(start_point, angle, length_shape):
#     for i in range(0, 361, 60):
#         vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
#         vector.draw()
#         start_point = vector.end_point
#
#
# point_triangle = sd.get_point(100, 100)
# angle_triangle = 0
# length_triangle = 200
#
# triangle(start_point=point_triangle, angle=angle_triangle, length_shape=length_triangle)
#
# point_square = sd.get_point(400, 100)
# angle_square = 0
# length_square = 200
#
# square(start_point=point_square, angle=angle_square, length_shape=length_square)
#
# point_pentagon = sd.get_point(200, 400)
# angle_pentagon = 36
# length_pentagon = 150
#
# pentagon(start_point=point_pentagon, angle=angle_pentagon, length_shape=length_pentagon)
#
# point_hexagon = sd.get_point(500, 400)
# angle_hexagon = 0
# length_hexagon = 150
#
# hexagon(start_point=point_hexagon, angle=angle_hexagon, length_shape=length_hexagon)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

def triangle(start_point, angle, length_shape):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=120)


def square(start_point, angle, length_shape):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=90)


def pentagon(start_point, angle, length_shape):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=72)


def hexagon(start_point, angle, length_shape):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=60)


def draw_vector(start_point, angle, length_shape, inner_angle):
    # start_point0 = start_point # убирает разрыв, но коряво
    # num_i = range(0, 360, inner_angle)[-2] # убирает разрыв, но коряво
    for i in range(0, 360, inner_angle):
        vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
        vector.draw()
        start_point = vector.end_point
        # if i == num_i: # убирает разрыв, но коряво
        #     break
    # sd.line(start_point=start_point, end_point=start_point0, color=sd.COLOR_RED, width=3) # убирает разрыв, но коряво


point_triangle = sd.get_point(500, 400)
angle_triangle = 0
length_triangle = 100
# triangle(start_point=point_triangle, angle=angle_triangle, length_shape=length_triangle)
# square(start_point=point_triangle, angle=angle_triangle, length_shape=length_triangle)
# pentagon(start_point=point_triangle, angle=angle_triangle, length_shape=length_triangle)
hexagon(start_point=point_triangle, angle=angle_triangle, length_shape=length_triangle)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.pause()
