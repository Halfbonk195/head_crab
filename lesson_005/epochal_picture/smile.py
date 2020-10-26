# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


def smile(x, y, color):
    # Рисуем эллипс
    left_bottom, right_top = sd.get_point(x, y), sd.get_point(x + 80, y + 60)
    sd.ellipse(left_bottom, right_top, color, 2)
    # Рисуем глазки
    sd.circle(sd.get_point(x + 25, y + 35), 7, color, 2)
    sd.circle(sd.get_point(x + 55, y + 35), 7, color, 2)
    # Рисуем рот
    sd.line(sd.get_point(x + 27, y + 14), sd.get_point(x + 40, y + 23), color, 2)
    sd.line(sd.get_point(x + 40, y + 23), sd.get_point(x + 53, y + 14), color, 2)
    # Рисуем нос
    sd.line(sd.get_point(x + 32, y + 30), sd.get_point(x + 48, y + 30), color, 2)
    sd.line(sd.get_point(x + 32, y + 30), sd.get_point(x + 40, y + 23), color, 2)
    sd.line(sd.get_point(x + 40, y + 23), sd.get_point(x + 48, y + 30), color, 2)
    # Рисуем ушки
    sd.line(sd.get_point(x + 10, y + 50), sd.get_point(x + 20, y + 80), color, 2)
    sd.line(sd.get_point(x + 20, y + 80), sd.get_point(x + 30, y + 57), color, 2)
    sd.line(sd.get_point(x + 68, y + 50), sd.get_point(x + 58, y + 80), color, 2)
    sd.line(sd.get_point(x + 58, y + 80), sd.get_point(x + 48, y + 57), color, 2)
    # Рисуем усики
    sd.line(sd.get_point(x + 25, y + 25), sd.get_point(x + (-10), y + 35), color, 2)
    sd.line(sd.get_point(x + 28, y + 22), sd.get_point(x + (-11), y + 20), color, 2)
    sd.line(sd.get_point(x + 25, y + 19), sd.get_point(x + (-8), y + 5), color, 2)
    sd.line(sd.get_point(x + 55, y + 25), sd.get_point(x + 90, y + 35), color, 2)
    sd.line(sd.get_point(x + 52, y + 22), sd.get_point(x + 91, y + 20), color, 2)
    sd.line(sd.get_point(x + 55, y + 19), sd.get_point(x + 88, y + 5), color, 2)