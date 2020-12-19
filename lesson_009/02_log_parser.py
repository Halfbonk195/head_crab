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


class LogParser:

    def __init__(self, file_name):
        self.file_name_r = file_name
        self.old_line = None
        self.count_NOK = 0
        self.count_OK = 0
        self.current_minute = None

    def action(self):
        file_name_w = 'sorted_' + self.file_name_r
        with open(self.file_name_r, 'r') as file_r:
            with open(file_name_w, 'w') as file_w:
                self.read_lines(file_r, file_w)

    def read_lines(self, file_r, file_w):
        for line in file_r:
            new_line = line[1:20] + line[28:]
            time_1 = time.strptime(new_line[0:19], "%Y-%m-%d %H:%M:%S")

            if self.current_minute is None:
                self.current_minute = time_1.tm_min

            if self.current_minute == time_1.tm_min:
                if 'NOK' in new_line:
                    self.count_NOK += 1
            else:
                time_old_struct = time.strptime(self.old_line[0:19], "%Y-%m-%d %H:%M:%S")
                time_old_str = time.strftime("%Y-%m-%d %H:%M:%S", time_old_struct)
                file_w.write(f'[{time_old_str}] {self.count_NOK}\n')
                if 'NOK' in new_line:
                    self.count_NOK = 1
                else:
                    self.count_NOK = 0
                self.current_minute = time_1.tm_min
            self.old_line = new_line


file_name_r = 'events.txt'
log_parser = LogParser(file_name_r)
log_parser.action()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
