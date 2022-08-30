"""Любимое число - сохраняет в файл и читает из файла"""
import json


def write_file(file_name, data):
    """Записывает data в файл с названием file_name в формате json"""
    with open(file_name, 'w') as f:
        json.dump(data, f)


def ask_user():
    """Просит пользователя ввести его любимое число"""
    while True:
        answer = input('Enter your favorite number: ')
        if answer.isnumeric():
            return answer
        else:
            print("You didn't enter a number!\n")


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
favorite_number = read_file(favorite_number_file_name)

if favorite_number:
    print(f'I know your favorite number! It is {favorite_number}!')
else:
    favorite_number = ask_user()
    write_file(favorite_number_file_name, favorite_number)
