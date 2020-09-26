# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1400, 800)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


width_line = 3
brick_dimensions = (100, 50)
color_brick = sd.COLOR_DARK_RED


def brick(start_p, end_p, color, width):
    sd.rectangle(start_p, end_p, color, width)


for x in range(0, sd.resolution[0], 100):
    for y in range(0, sd.resolution[1], 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + brick_dimensions[0], y + brick_dimensions[1])
        brick(start_point, end_point, color_brick, width_line)

    for y in range(50, sd.resolution[1], 100):
        start_point = sd.get_point(x + 50, y)
        end_point = sd.get_point(x + brick_dimensions[0] + 50, y + brick_dimensions[1])
        brick(start_point, end_point, color_brick, width_line)

sd.pause()
