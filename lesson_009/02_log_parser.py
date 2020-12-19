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
        self.file_r = None
        self.file_w = None
        self.old_line = None
        self.count_NOK = 0
        self.count_OK = 0
        self.current_time = None
        self.file_name_w = 'sorted_' + file_name

    def open_file(self, name, mod):
        if mod == 'r':
            self.file_r = open(name, mode=mod)
        else:
            self.file_w = open(name, mode=mod)

    @staticmethod
    def close_file(name):
        name.close()

    def action(self):
        self.open_file(self.file_name_r, 'r')
        self.open_file(self.file_name_w, 'w')
        self.read_lines()
        self.close_file(self.file_r)
        self.close_file(self.file_w)

    def read_lines(self):
        for line in self.file_r:
            new_line = line[1:20] + line[28:]
            time_1 = time.strptime(new_line[0:19], "%Y-%m-%d %H:%M:%S")
            sorted_mod_str, time_past = self.sort_mod(time_1)
            self.write_sorted_lines(time_past, new_line, sorted_mod_str)
            self.old_line = new_line

        time_old_struct = time.strptime(self.old_line[0:19], "%Y-%m-%d %H:%M:%S")
        time_old_str = time.strftime(sorted_mod_str, time_old_struct)
        self.file_w.write(f'[{time_old_str}] {self.count_NOK}\n')

    def write_sorted_lines(self, time_past, new_line, sorted_mod_str):
        if self.current_time is None:
            self.current_time = time_past

        if self.current_time == time_past:
            if 'NOK' in new_line:
                self.count_NOK += 1
        else:
            time_old_struct = time.strptime(self.old_line[0:19], "%Y-%m-%d %H:%M:%S")
            time_old_str = time.strftime(sorted_mod_str, time_old_struct)
            self.file_w.write(f'[{time_old_str}] {self.count_NOK}\n')
            if 'NOK' in new_line:
                self.count_NOK = 1
            else:
                self.count_NOK = 0
            self.current_time = time_past

    def sort_mod(self, time_for_convert):
        sorted_mod_str = '%Y-%m-%d %H:%M:%S'
        time_new = time_for_convert.tm_sec
        return sorted_mod_str, time_new


class LogParserMin(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.file_name_w = 'sorted_min_' + file_name

    def sort_mod(self, time_for_convert):
        sorted_mod_str = '%Y-%m-%d %H:%M'
        time_new = time_for_convert.tm_min
        return sorted_mod_str, time_new


class LogParserHour(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.file_name_w = 'sorted_hour_' + file_name

    def sort_mod(self, time_for_convert):
        sorted_mod_str = '%Y-%m-%d %H'
        time_new = time_for_convert.tm_hour
        return sorted_mod_str, time_new


class LogParserMonth(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.file_name_w = 'sorted_mon_' + file_name

    def sort_mod(self, time_for_convert):
        sorted_mod_str = '%Y-%m'
        time_new = time_for_convert.tm_mon
        return sorted_mod_str, time_new


class LogParserYear(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.file_name_w = 'sorted_year_' + file_name

    def sort_mod(self, time_for_convert):
        sorted_mod_str = '%Y'
        time_new = time_for_convert.tm_year
        return sorted_mod_str, time_new


file_name_r = 'events.txt'
# log_parser_min = LogParserMin(file_name_r)
# log_parser_hour = LogParserHour(file_name_r)
log_parser_mon = LogParserMonth(file_name_r)
log_parser_year = LogParserYear(file_name_r)
# log_parser_min.action()
# log_parser_hour.action()
log_parser_mon.action()
log_parser_year.action()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
