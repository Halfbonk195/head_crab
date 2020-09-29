# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (1400, 900)


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


Figures = {
    1: 'Triangle',
    2: 'Square',
    3: 'Pentagon',
    4: 'hexagon',
}
angle = 10
point = sd.get_point(600, 500)
print('Возможные фигуры:')
for key, value in Figures.items():
    print(str(key) + ' : ' + value)

while True:
    num_figure = input('Введите номер желаемой фигуры > ')
    if not num_figure.isnumeric():
        print('Вы ввели не цифры или нецелое число! Ай-ай-ай... Давайте заново.')
        continue
    else:
        num_figure = int(num_figure)

    if num_figure < 1 or num_figure > 4:
        print('Вы ввели некорректный номер фигуры! Посмотри! Там нужно ввести от 1 до 4.\n'
              'Давай еще раз ;)')
        continue
    else:
        if num_figure == 1:
            length = 220
            triangle(start_point=point, angle=angle, length_shape=length)
        elif num_figure == 2:
            length = 200
            square(start_point=point, angle=angle, length_shape=length)
        elif num_figure == 3:
            length = 180
            pentagon(start_point=point, angle=angle, length_shape=length)
        else:
            length = 150
            hexagon(start_point=point, angle=angle, length_shape=length)

        break


sd.pause()
