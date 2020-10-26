# -*- coding: utf-8 -*-
"""
    Модуль для рисования стены из кирпичей v1.0
"""

import simple_draw as sd


def brick(start_p, end_p, brick_dimensions, color=sd.COLOR_YELLOW, width=1):
    """
        Строит стену из кирпичей цветом color, толщиной width
        start_p - нижний левый угол стены, тип (x, y)
        end_p - верхний правый угол стены, тип (x, y)
        brick_dimensions - размер кирпича (x, y)
    """

    for x in range(start_p[0], end_p[0], brick_dimensions[0]):
        for y in range(start_p[1], end_p[1], brick_dimensions[1] * 2):
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x + brick_dimensions[0], y + brick_dimensions[1])
            sd.rectangle(start_point, end_point, color, width)

        for y in range(start_p[1] + brick_dimensions[1], end_p[1], brick_dimensions[1] * 2):
            start_point = sd.get_point(x + brick_dimensions[0] // 2, y)
            end_point = sd.get_point(x + brick_dimensions[0] + brick_dimensions[0] // 2, y + brick_dimensions[1])
            sd.rectangle(start_point, end_point, color, width)

