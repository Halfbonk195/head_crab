"""Любимое число (запрашивает у пользователя и записывает в файл)"""
import json


def write_file(file_name, data):
    """Записывает data в файл с названием file_name в формате json"""
    with open(file_name, 'w') as f:
        json.dump(data, f)


def ask_user():
    answer = input('Enter your favorite number: ')
    return answer


favorite_number_file_name = 'favorite_number.txt'
favorite_number = ask_user()
write_file(favorite_number_file_name, favorite_number)
