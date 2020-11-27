from newton_engine import find_partial_diff, newton_method
from sympy import symbols, cos, sin


def f1(x, y):
    return sin(2*x - y) - 1.2*x - 0.4


def f2(x, y):
    return 0.8 * x**2 + 1.5 * y**2 - 1


x_symb, y_symb = symbols('x, y')
diff_dict = find_partial_diff(f1(x_symb, y_symb), f2(x_symb, y_symb))
for key in diff_dict:
    print(key, '=', diff_dict[key])

x_num = 0.4
y_num = -0.75
n_eps = 4
eps = 0.1 ** n_eps

x_end, y_end, iteration = newton_method(x_num, y_num, eps)
print('\nОтвет: x =', round(x_end, n_eps), 'y =', round(y_end, n_eps), 'количество итераций =', iteration)
