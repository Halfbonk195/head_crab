"""Модуль ищет количество вхождений конкретного слова в текстовый файл"""


def reading_file(file_name):
    """Функция читает файл file_name и возвращает содержимое в списке"""
    with open(file_name, 'r', encoding='utf-8') as f:
        f_strings = f.readlines()
    print(f"Read file '{file_name}':")
    return f_strings


my_file = 'The_weight_of_the_name.txt'
count_my_word = 0
my_word = 'the'

try:
    strings = reading_file(my_file)
except FileNotFoundError:
    print(f"No such file '{my_file}'!")
else:
    for line in strings:
        count_my_word += line.lower().count(my_word.lower())
    print(f"The text '{my_file}' contains {count_my_word} words '{my_word}'")
