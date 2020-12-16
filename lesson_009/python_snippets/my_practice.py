# Прочитать зип файл
import zipfile
from pprint import pprint
from random import randint, choice


class Chaterer():

    def __init__(self, size_combination, N_chars):
        self.file_for_statistics = None
        self.statistics = {}
        self.first_combine_of_char = None
        self.size_combination = size_combination
        self.N_chars = N_chars
        self.totals_chars = {}
        self.sorted_statistics = {}


    def __str__(self):
        return ''

    def read_file(self, file_name):
        if zipfile.is_zipfile(file_name):
            self.unzip(file_name)
        else:
            self.file_for_statistics = file_name

    def unzip(self, file):
        zip_file = zipfile.ZipFile(file, 'r')
        for file_in_zip in zip_file.namelist():
            zip_file.extract(file_in_zip)
            self.file_for_statistics = file_in_zip

    def collect_statistics(self):
        with open(self.file_for_statistics, 'r', encoding='cp1251') as _file:
            tmp_char = _file.read(self.size_combination)
            self.first_combine_of_char = tmp_char
            for line in _file:
                for char in line:
                    if tmp_char in self.statistics:
                        if char in self.statistics[tmp_char]:
                            self.statistics[tmp_char][char] += 1
                        else:
                            self.statistics[tmp_char][char] = 1
                    else:
                        self.statistics[tmp_char] = {char: 1}
                    tmp_char = tmp_char[1:] + char

    def sort_statistics(self):
        for key, value in self.statistics.items():
            self.sorted_statistics[key] = []
            self.totals_chars[key] = 0
            for key_inner, value_inner in value.items():
                self.totals_chars[key] += value_inner
                self.sorted_statistics[key].append([value_inner, key_inner])
                self.sorted_statistics[key].sort(reverse=True)

    def chat(self):
        printed = 0
        space = 0
        while printed <= self.N_chars:

            dice = randint(1, self.totals_chars[self.first_combine_of_char])
            position = 0
            for value, char in self.sorted_statistics[self.first_combine_of_char]:
                position += value
                if dice <= position:
                    break
            self.first_combine_of_char = self.first_combine_of_char[1:] + char
            if char == ' ':
                space += 1
            if char == '\n':
                continue
            if space >= 15:
                space = 0
                print()
            print(char, end='')
            printed += 1

SIZE = 6
N_CHARS = 2000

chaterer = Chaterer(size_combination=SIZE, N_chars=N_CHARS)
chaterer.read_file('voyna-i-mir.txt')
chaterer.collect_statistics()
chaterer.sort_statistics()
chaterer.chat()
