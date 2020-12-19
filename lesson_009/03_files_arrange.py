# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class SortMyPhoto:

    def __init__(self, dir_for_scan, dir_for_copy):
        self.dir_read = os.path.normpath(dir_for_scan)
        self.dir_write = os.path.normpath(dir_for_copy)
        self.files_dict = {}
        self.sorted_files_dict = {}

    def __str__(self):
        return 'Я сортирую фотки по годам и месяцам'

    def scan_dir(self):
        """Сканирует дирикторию и запоминает пути и дату до файлов"""

        for dirpath, dirnames, filenames in os.walk(self.dir_read):
            for file in filenames:
                full_path = os.path.join(dirpath, file)
                full_path = os.path.normpath(full_path)

                file_time = os.path.getmtime(full_path)
                file_time = time.gmtime(file_time)
                year = time.strftime('%Y', file_time)
                month = time.strftime('%m', file_time)

                self.files_dict[file] = {'path': full_path, 'year': year, 'month': month, }

    def sort_files(self):
        """Сортирует все файлы и их характеристики в словарь вида {год:{месяц:[file_name1, file_name2, ...]}}"""

        for file_name, file_value in self.files_dict.items():
            year = file_value['year']
            mon = file_value['month']
            if year in self.sorted_files_dict:
                if mon in self.sorted_files_dict[year]:
                    self.sorted_files_dict[year][mon].append(file_name)
                else:
                    self.sorted_files_dict[year][mon] = [file_name]
            else:
                self.sorted_files_dict[year] = {mon: [file_name]}

    def copy_files(self):
        """Создает директории год/месяц и копирует по ним файлы"""

        print(f'Всего лет: {self.sorted_files_dict.keys()}')
        for year, other_value in self.sorted_files_dict.items():
            print(f'Началось копирование {year} года')

            for mon, file_names in other_value.items():
                dir_path = os.path.join(self.dir_write, year, mon)
                os.makedirs(dir_path, exist_ok=True)

                for file_name in file_names:
                    src_path = self.files_dict[file_name]['path']
                    shutil.copy2(src_path, dir_path)


path_for_scan = 'C:/Users/halfb/Desktop/Test'
path_for_copy = 'C:/Users/halfb/Desktop/Test/sort'

sort_my_files = SortMyPhoto(path_for_scan, path_for_copy)
sort_my_files.scan_dir()
sort_my_files.sort_files()
sort_my_files.copy_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
