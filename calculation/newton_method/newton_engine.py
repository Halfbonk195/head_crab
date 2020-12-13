from sympy import symbols, diff, lambdify
import numpy as np

_diff_dict = {}
_diff_numeric = {}
_solution_linear_eqs = []

def find_partial_diff(f1, f2):
    """Находит частные производные по 2-м функциям и записывает их в словарь"""
    global _diff_dict
    _diff_dict = {}

    x, y = symbols('x, y')
    _diff_dict['f1'] = f1
    _diff_dict['f2'] = f2
    _diff_dict['df1x'] = diff(f1, x)
    _diff_dict['df2x'] = diff(f2, x)
    _diff_dict['df1y'] = diff(f1, y)
    _diff_dict['df2y'] = diff(f2, y)

    return _diff_dict


def find_partial_diff_numeric(x_num, y_num):
    """Конвертирует символьные производные в норальные функции
       и находит численное значение в точке (x_num, y_num)
       записывает в _diff_numeric"""

    global _diff_numeric
    _diff_numeric = {}
    x, y = symbols('x, y')
    for key in _diff_dict:
        f = _diff_dict[key]
        f = lambdify([x, y], f, 'numpy')
        _diff_numeric[key] = f(x_num, y_num)
    print(_diff_numeric)
    return _diff_numeric


def write_matrix():
    matrix = [[], []]
    matrix[0].append(_diff_numeric['df1x'])
    matrix[0].append(_diff_numeric['df1y'])
    matrix[0].append(-_diff_numeric['f1'])
    matrix[1].append(_diff_numeric['df2x'])
    matrix[1].append(_diff_numeric['df2y'])
    matrix[1].append(-_diff_numeric['f2'])
    return matrix


def solve_linear_eqs(matrix):
    """Решает систему из 2-х линейных уравнений"""
    global _solution_linear_eqs
    _solution_linear_eqs = []

    delta = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    delta_x = matrix[0][2] * matrix[1][1] - matrix[0][1] * matrix[1][2]
    delta_y = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]

    _solution_linear_eqs.append(delta_x/delta)
    _solution_linear_eqs.append(delta_y/delta)
    return None


def newton_method(x, y, eps):
    x1 = x + 1
    y1 = y + 1
    counter_iter = 0
    while abs(x1 - x) >= eps and abs(y1 - y) >= eps:
        x1 = x
        y1 = y
        find_partial_diff_numeric(x, y)
        matrix = write_matrix()
        solve_linear_eqs(matrix)

        g_n = _solution_linear_eqs[0]
        h_n = _solution_linear_eqs[1]

        x += g_n
        y += h_n

        counter_iter += 1
        print('x_{} = {}, y_{} = {}'.format(counter_iter, round(x, 4), counter_iter, round(y, 4)))
    return x, y, counter_iter
