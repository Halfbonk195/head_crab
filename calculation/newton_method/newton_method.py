from newton_engine import find_partial_diff, newton_method
from sympy import symbols, cos, sin, plot_implicit, Eq, Or


def f1(x, y):
    return sin(2*x - y) - 1.2*x - 0.4


def f2(x, y):
    return 0.8 * x**2 + 1.5 * y**2 - 1


x_symb, y_symb = symbols('x, y')
diff_dict = find_partial_diff(f1(x_symb, y_symb), f2(x_symb, y_symb))
for key in diff_dict:
    print(key, '=', diff_dict[key])
plot_implicit(Or(Eq(f1(x_symb, y_symb), 0), Eq(f2(x_symb, y_symb), 0)), (x_symb, -3, 3), (y_symb, -3, 3))

x_num = -1.1
y_num = -0.2
n_eps = 4
eps = 0.1 ** n_eps


x_end, y_end, iteration = newton_method(x_num, y_num, eps)
print('\nОтвет: x =', round(x_end, n_eps), 'y =', round(y_end, n_eps), 'количество итераций =', iteration)
