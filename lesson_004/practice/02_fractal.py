# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 800)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(400, 5)


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


# angle_0 = 90
# length_0 = 200
# next_point = branch(point_0, angle_0, length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов
# angle_0 = 90
# length_0 = 200
#
# next_angle = angle_0
# next_length = length_0
# next_point = point_0
#
# while next_length > 1:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 35
#     next_length = next_length * .75

# сделать функцию branch рекурсивной


def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
angle_0 = 50
for length in range(100, 301, 10):
    for delta in range(0, angle_0 + 1, 10):
        branch(point=point_0, angle=90, length=length, delta=delta)
    for delta in range(-1 * angle_0 - 1, 1, 10):
        branch(point=point_0, angle=90, length=length, delta=delta)
    angle_0 += 10

sd.pause()

