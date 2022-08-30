"""Любимое число (запрашивает у пользователя и записывает в файл)"""
import json


def read_file(file_name):
    """Получает данные из файла в формате json, если он существует"""
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return data


favorite_number_file_name = 'favorite_number.txt'
your_favorite_number = read_file(favorite_number_file_name)

if your_favorite_number:
    print(f'I know your favorite number! It is {your_favorite_number}!')
