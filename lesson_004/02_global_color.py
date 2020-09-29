# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1400, 900)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def triangle(start_point, angle, length_shape, color):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=120, color=color)


def square(start_point, angle, length_shape, color):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=90, color=color)


def pentagon(start_point, angle, length_shape, color):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=72, color=color)


def hexagon(start_point, angle, length_shape, color):
    draw_vector(start_point=start_point, angle=angle, length_shape=length_shape, inner_angle=60, color=color)


def draw_vector(start_point, angle, length_shape, inner_angle, color):
    # start_point0 = start_point # убирает разрыв, но коряво
    # num_i = range(0, 360, inner_angle)[-2] # убирает разрыв, но коряво
    for i in range(0, 360, inner_angle):
        vector = sd.get_vector(start_point=start_point, angle=angle + i, length=length_shape, width=3)
        vector.draw(color=color)
        start_point = vector.end_point
        # if i == num_i: # убирает разрыв, но коряво
        #     break
    # sd.line(start_point=start_point, end_point=start_point0, color=sd.COLOR_RED, width=3) # убирает разрыв, но коряво


color_list = {
    1: [sd.COLOR_RED, 'Red'],
    2: [sd.COLOR_ORANGE, 'Orange'],
    3: [sd.COLOR_YELLOW, 'Yellow'],
    4: [sd.COLOR_GREEN, 'Green'],
    5: [sd.COLOR_CYAN, 'Cyan'],
    6: [sd.COLOR_BLUE, 'Blue'],
    7: [sd.COLOR_PURPLE, 'Purple']
}
angle = 10

print('Возможные цвета:')
for key, value in color_list.items():
    print(str(key) + ' : ' + value[1])

while True:
    num_color = input('Введите желаемый цвет > ')
    if not num_color.isnumeric():
        print('Вы ввели не цифры или нецелое число! Ай-ай-ай... Давайте заново.')
        continue
    else:
        num_color = int(num_color)

    if num_color < 1 or num_color > 7:
        print('Вы ввели некорректный номер цвета! Посмотри! Там нужно ввести от 1 до 7. Это не сложно, давай еще раз ;)')
        continue
    else:
        point, length = sd.get_point(300, 200), 200
        triangle(start_point=point, angle=angle, length_shape=length, color=color_list[num_color][0])
        point, length = sd.get_point(800, 200), 180
        square(start_point=point, angle=angle, length_shape=length, color=color_list[num_color][0])
        point, length = sd.get_point(300, 600), 150
        pentagon(start_point=point, angle=angle, length_shape=length, color=color_list[num_color][0])
        point, length = sd.get_point(800, 600), 120
        hexagon(start_point=point, angle=angle, length_shape=length, color=color_list[num_color][0])
        break

sd.pause()
