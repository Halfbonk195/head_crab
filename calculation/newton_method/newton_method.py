import sys
import math, numpy
from sympy import symbols, tanh, diff, lambdify, cos, sin
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


def f1(x, y):
    return cos(y+0.5) +x -0.8


def f2(x, y):
    return sin(x) - 2*y - 1.6


def diff_f1x(x, y):
    return 1


def diff_f1y(x, y):
    return -sin(y + 0.5)


def diff_f2x(x, y):
    return cos(x)


def diff_f2y(x, y):
    return -2



def Newton(x, y, eps):
    x1 = x * 100
    y1 = y * 100
    counter_iter = 0
    while abs(x1 - x) > eps and abs(y1 - y) > eps:
        x1 = x
        y1 = y
        delta = diff_f1x(x, y)*diff_f2y(x, y) - diff_f1y(x, y)*diff_f2x(x, y)
        delta_x = -f1(x, y)*diff_f2y(x, y) + diff_f1y(x,y)*f2(x, y)
        delta_y = -diff_f1x(x, y)*f2(x, y) + f1(x, y)*diff_f2x(x, y)

        g_n = delta_x/delta
        h_n = delta_y/delta

        x += g_n
        y += h_n
        counter_iter += 1

    return x, y, counter_iter


x = -0.1
y = -0.8
eps = 0.0001
solv = Newton(x=x, y=y, eps=eps)

print('x = {}, y = {}, i = {}'.format(round(solv[0], 3), round(solv[1], 3), solv[2]))

