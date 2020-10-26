# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import epochal_picture.wall as wall
import epochal_picture.shapes as shapes
import epochal_picture.trees as trees
import epochal_picture.smile as smile


sd.resolution = (1400, 1000)
# Строим бек граунт
sd.background_color = sd.COLOR_ORANGE
sd.rectangle(left_bottom=sd.get_point(0, 650), right_top=sd.get_point(1400, 1000), width=0, color=sd.COLOR_DARK_CYAN)

# Строим дом
# Строим стену дома
sd.rectangle(left_bottom=sd.get_point(500, 150),
             right_top=sd.get_point(800 + 40, 350), color=sd.COLOR_DARK_RED, width=0)
wall.brick(start_p=(500, 150), end_p=(800, 350), width=2, color=sd.COLOR_DARK_ORANGE, brick_dimensions=(40, 20))
sd.rectangle(left_bottom=sd.get_point(500, 150),
             right_top=sd.get_point(800 + 40, 350), color=sd.COLOR_BLACK, width=3)
# Строим крышу дома
hight_roof = 100
roof_start_p = (470, 350)
len_roof = 400
for x in range(0, 401, 18):  # Закраска крыши
    start_p = sd.get_point(roof_start_p[0] + (len_roof - x) / 2, roof_start_p[1] + hight_roof / 2 * (1 - x / len_roof))
    tmp_hight = hight_roof * x / len_roof
    shapes.triangle(start_point=start_p, length_shape=x, width=4, hight=tmp_hight, color=sd.COLOR_RED)
shapes.triangle(start_point=start_p, length_shape=len_roof, width=4, hight=hight_roof, color=sd.COLOR_BLACK)
# Конец постройки дома

# Строим деревья
for x in range(300, 1300, 80):  # Дальний план
    for y in range(600, 640, 10):
        trees.get_tree(point=sd.get_point(x + sd.random_number(-25, 25), y + sd.random_number(0, 20)),
                       length=30 + sd.random_number(0, 8))

trees.get_tree(point=sd.get_point(1100, 150), length=110)   # Дерево на переднем плане
# Конец постройки деревьев

# Строим смайлик
smile.smile(x=870, y=160, color=sd.COLOR_BLACK)

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
