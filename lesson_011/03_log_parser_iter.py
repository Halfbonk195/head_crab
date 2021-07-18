# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class LogParser:

    def __init__(self, file_name):
        self.file_name_r = file_name
        self.file_r = None
        self.old_line = None
        self.event_count = 0
        self.group_time = None
        self.end = None

    def __iter__(self):
        self.file_r = open(self.file_name_r, mode='r')
        self.event_count = 0
        self.end = None
        return self

    def __next__(self):
        if self.end:
            self.file_r.close()
            raise StopIteration()

        while True:
            new_line = self.file_r.readline()

            if not new_line:
                self.group_time = self.old_line
                sent_event_count = self.event_count
                self.end = True
                break

            new_line_date, new_line_event = self.line_processing(new_line)

            if self.old_line != new_line_date and self.old_line is not None:
                self.group_time = self.old_line
                self.old_line = new_line_date
                sent_event_count = self.event_count
                self.event_count = 0
                if 'NOK' in new_line_event:
                    self.event_count += 1

                break

            if 'NOK' in new_line_event:
                self.event_count += 1
            self.old_line = new_line_date

        return self.group_time, sent_event_count

    @staticmethod
    def line_processing(line):
        new_line_date = line[1:17]
        new_line_event = line[29:-1]

        return new_line_date, new_line_event


file_name_r = 'events.txt'

grouped_events = LogParser(file_name_r)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
