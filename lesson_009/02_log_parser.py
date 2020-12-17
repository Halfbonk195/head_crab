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
        current_minute = None

        for line in file_r:
            new_line = line[1:20] + line[28:]

            time_1 = time.strptime(new_line[0:19], "%Y-%m-%d %H:%M:%S")
            if current_minute is None:
                current_minute = time_1.tm_min

            if current_minute == time_1.tm_min:
                if 'NOK' in new_line:
                    count_NOK += 1
            else:
                file_w.write(f'[{old_line[:17]}] {count_NOK}\n')
                if 'NOK' in new_line:
                    count_NOK = 1
                else:
                    count_NOK = 0
                current_minute = time_1.tm_min
            old_line = new_line



# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
