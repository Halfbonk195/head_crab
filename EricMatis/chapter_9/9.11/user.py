"""Создает простого пользователя и администратора"""


class User:
    """Создает пользователя с некоторым набором информации"""

    def __init__(self, first_name, last_name, e_mail, age, login):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.e_mail = e_mail
        self.age = age
        self.login = login
        self.login_attempts = 0

    def describe_user(self):
        """Выводит информацию о пользователе"""

        print(f'User name: {self.first_name} {self.last_name}')
        print(f'User age: {self.age}')
        print(f'User e-mail: {self.e_mail}')
        print(f'User login: {self.login}')
        print('\n')

    def greet_user(self):
        """Приветствует пользователя"""

        print(f'Приветствуем тебя, {self.first_name} {self.last_name}! Мы скучали.')
        print('----------------------------------------------')

    def increment_login_attempts(self):
        """Суммирует количество попыток входа"""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество поптыток входа"""

        self.login_attempts = 0
