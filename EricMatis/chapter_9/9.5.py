class User:
    """Создает пользователя с некоторым набором информации"""

    def __init__(self, first_name, last_name, e_mail, age, login):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.login = login
        self.login_attempts = 0

    def describe_user(self):
        """Выводит информацию о пользователе"""

        print(f'User name: {self.first_name.title()} {self.last_name.title()}')
        print(f'User age: {self.age}')
        print(f'User e-mail: {self.e_mail}')
        print(f'User login: {self.login}')

    def greet_user(self):
        """Приветствует пользователя"""

        print(f'Hello, {self.first_name.title()} {self.last_name.title()}! We were waiting for you.')
        print('----------------------------------------------')

    def increment_login_attempts(self):
        """Суммирует количество попыток входа"""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество поптыток входа"""

        self.login_attempts = 0


viktor = User('Viktor', 'Komarov', 'V.komarov@mail.ru', 27, 'manyak')
viktor.increment_login_attempts()
viktor.increment_login_attempts()
viktor.increment_login_attempts()
viktor.increment_login_attempts()
viktor.increment_login_attempts()
print(f'Количество попыток входа - {viktor.login_attempts}\n')

viktor.describe_user()
viktor.greet_user()

viktor.reset_login_attempts()
print(f'Количество попыток входа - {viktor.login_attempts}\n')
