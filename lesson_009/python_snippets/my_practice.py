# Прочитать зип файл
import zipfile
from pprint import pprint
from random import randint, choice

my_file = 'voyna-i-mir.txt.zip'
zip_file = zipfile.ZipFile(my_file, 'r')
# Распаковать зип файл

for file_name in zip_file.namelist():
    zip_file.extract(file_name)

# Посчитать количество повторений букв и записать в словарь
number_of_different_letters = {}


number_letters_combined = 15
with open(file_name, 'r', encoding='cp1251') as file:
    tmp_char = file.read(number_letters_combined)
    first_char = tmp_char
    for line in file:
        for char in line:
            if tmp_char in number_of_different_letters:
                if char in number_of_different_letters[tmp_char]:
                    number_of_different_letters[tmp_char][char] += 1
                else:
                    number_of_different_letters[tmp_char][char] = 1
            else:
                number_of_different_letters[tmp_char] = {char: 1}
            tmp_char = tmp_char[1:] + char

# pprint(number_of_different_letters)

# Отсортировать массивы, на первое место в списке поставить наиболее часто встречающиеся буквы

totals_chars = {}
sorted_statistics = {}
all_keys = []
for key, value in number_of_different_letters.items():
    sorted_statistics[key] = []
    totals_chars[key] = 0
    for key_inner, value_inner in value.items():
        totals_chars[key] += value_inner
        sorted_statistics[key].append([value_inner, key_inner])
        sorted_statistics[key].sort(reverse=True)
    all_keys.append(key)


# pprint(sorted_statistics)
# pprint(totals_chars)


# Генерировать на консоль слова

N_chars = 10000
printed = 0
space = 0
while printed <= N_chars:

    dice = randint(1, totals_chars[first_char])
    position = 0
    for value, char in sorted_statistics[first_char]:
        position += value
        if dice <= position:
            break
    if char == ' ':
        space += 1
    if space >= 10:
        space = 0
        print()
    print(char, end='')
    first_char = first_char[1:] + char
    printed += 1

