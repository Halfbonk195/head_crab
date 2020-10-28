# -*- coding: utf-8 -*-
"""
    Модуль рисования радуги
"""

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow(point, width, radius):
    for color in rainbow_colors:
        sd.circle(point, radius, color, width)
        radius += width
