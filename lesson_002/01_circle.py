#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

square = 3.1415926 * radius ** 2
print(round(square, 4))

# Далее, пусть есть координаты точки
point = (30, 26)

# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
point_0 = (0, 0)
distance_from_center = ((point[0] - point_0[0]) ** 2 + (point[1] - point_0[1]) ** 2) ** .5
belong_to = distance_from_center < radius
print(belong_to)
print('Расстояние от первой точки до центра круга =', round(distance_from_center, 4))

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
distance_from_center = ((point_2[0] - point_0[0]) ** 2 + (point_2[1] - point_0[1]) ** 2) ** .5
belong_to = distance_from_center < radius
print(belong_to)
print('Расстояние от второй точки до центра круга =', round(distance_from_center, 4))
# Пример вывода на консоль:
#
# 77777.7777
# False
# False


