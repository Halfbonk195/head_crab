# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()
point_0 = sd.get_point(100, 500)

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
y = 500
x = 100

y2 = 450
x2 = 150

y3 = 470
x3 = 200

y4 = 480
x4 = 250

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 5
    if y < 50:
        break
    x += sd.randint(0, 30)

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 5
    if y2 < 50:
        break
    x2 += sd.randint(0, 25)

    point3 = sd.get_point(x3, y3)
    sd.snowflake(center=point3, length=50)
    y3 -= 5
    if y3 < 50:
        break
    x3 += sd.randint(0, 35)

    point4 = sd.get_point(x4, y4)
    sd.snowflake(center=point4, length=50)
    y4 -= 5
    if y4 < 50:
        break
    x4 += sd.randint(0, 35)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#        break
#     x = x + 10
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 50:
#        break
#     x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
