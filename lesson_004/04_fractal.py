# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# sd.resolution = (1400, 800)
#
#
# def branch_draw(point, angle, length):
#     if length < 5:
#         return
#     step_angle = 30
#     v1 = sd.get_vector(start_point=point, angle=angle - step_angle, length=length, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle + step_angle, length=length, width=2)
#     v2.draw()
#     length *= 0.75
#     branch_draw(point=v1.end_point, angle=angle - step_angle, length=length)
#     branch_draw(point=v2.end_point, angle=angle + step_angle, length=length)
#
#
# point_0 = sd.get_point(700, 30)
# root_point = sd.get_point(700, 0)
# angle = 90
# length = 200
# sd.get_vector(start_point=root_point, angle=angle, length=30, width=2).draw()
# branch_draw(point=point_0, angle=angle, length=length)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


sd.resolution = (1400, 800)


def branch_draw(point, angle, length):
    if length < 5:
        return
    if 100 <= length < 150:
        width = 6
    elif 50 <= length < 100:
        width = 3
    elif length < 50:
        width = 1
    else:
        width = 7
    step_angle = 30 + sd.random_number(-12, 12)
    v1 = sd.get_vector(start_point=point, angle=angle - step_angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle + step_angle, length=length, width=width)
    v2.draw()
    length *= (1 + sd.random_number(-20, 20) / 100) * 0.75
    branch_draw(point=v1.end_point, angle=angle - step_angle, length=length)
    branch_draw(point=v2.end_point, angle=angle + step_angle, length=length)


point_0 = sd.get_point(700, 30)
root_point = sd.get_point(700, 0)
angle = 90
length = 200
sd.get_vector(start_point=root_point, angle=angle, length=30, width=7).draw()
branch_draw(point=point_0, angle=angle, length=length)




sd.pause()


