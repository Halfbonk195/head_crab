# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
snowflake_list = list()
i = 0
while i < N:  # задаём начальные положения N снежинок с рандомными отклонениями и по x и по y и рандомной длинной
    x_0 = 1100 * (i + 1) // N + sd.random_number(-20, 20)
    y_0 = 700 + sd.random_number(-50, 50)
    len_flake = sd.random_number(10, 100)
    snowflake_list.append([x_0, y_0, len_flake])
    i += 1

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# while True:
#     sd.clear_screen()
#     for _, prms_flake in enumerate(snowflake_list):
#         point = sd.get_point(prms_flake[0], prms_flake[1])
#         sd.snowflake(center=point, length=prms_flake[2])
#         prms_flake[1] -= sd.random_number(3, 10)
#         prms_flake[0] += sd.random_number(-20, 20)
#
#     if prms_flake[1] < 50:
#         break
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
def draw_snowflake(point):
    while True:
        sd.clear_screen()
        sd.snowflake(center=point, length=50)
        point.y -= sd.random_number(5, 10)

        if point.y < 50:
            break
    sd.sleep(0.1)


while True:
    x = sd.random_number(50, 1100)
    y = 700
    point = sd.get_point(x, y)
    draw_snowflake(point=point)
    if sd.user_want_exit():
        break

sd.pause()
