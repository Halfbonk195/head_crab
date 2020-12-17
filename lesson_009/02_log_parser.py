# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import time

file_name_r = 'events.txt'
file_name_w = 'sorted_events.txt'

with open(file_name_r, 'r') as file_r:
    with open(file_name_w, 'w') as file_w:

        old_line = None
        count_NOK = 0
        count_OK = 0
        for line in file_r:
            new_line = ''
            CUT = False
            for char in line:
                if char == ']':
                    CUT = False

                if char == '.' or CUT:
                    CUT = True
                    continue
                else:
                    new_line += char

            eq = False
            if old_line:
                time_1 = time.strptime(new_line[1:20], "%Y-%m-%d %H:%M:%S")
                time_2 = time.strptime(old_line[1:20], "%Y-%m-%d %H:%M:%S")

                if time_1.tm_min == time_2.tm_min:
                    if new_line[-3:] == old_line[-3:]:
                        if new_line[-4:-1] == 'NOK':
                            count_NOK += 1
                        else:
                            count_OK += 1
                        eq = True
                if eq:
                    pass
                else:
                    if count_NOK:
                        print(f'{old_line[0:17]}] {count_NOK}')
                        count_NOK = 0
            elif new_line[-4:-1] == 'NOK':
                count_NOK = 1
            old_line = new_line

            result_time = time.strptime(new_line[1:20], "%Y-%m-%d %H:%M:%S")
            time_start = result_time

            quantity_OK = 0

            # file_w.write(new_line)
            # print(new_line)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
