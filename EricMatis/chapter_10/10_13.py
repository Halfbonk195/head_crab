import json


def get_stored_username(file):
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user(file):
    """Приветствует пользователя по имени."""
    username = get_stored_username(file)
    if username:
        answer = input(f'Are you {username}? (y/n): ')
        if answer == 'y':
            print(f'Welcome back, {username}!')
        else:
            username = get_new_username(file)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(file)
        print(f"We'll remember you when you come back, {username}!")


def get_new_username(file):
    """Запрашивает новое имя пользователя."""
    username = input('What is your name? ')
    with open(file, 'w') as f:
        json.dump(username, f)
    return username


filename = 'username.json'
greet_user(filename)
