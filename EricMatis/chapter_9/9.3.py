class User:
    """Создает пользователя с некоторым набором информации"""

    def __init__(self, first_name, last_name, e_mail, age, login):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.login = login

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


viktor = User('Viktor', 'Komarov', 'V.komarov@mail.ru', 27, 'manyak')
andrey = User('Andrey', 'potemkin', 'nagibator@mail.ru', 65, 'lollipop')
den = User('Den', 'Raygon', 'rassia_is_big@gmail.com', 23, 'dart_wayder')

viktor.describe_user()
viktor.greet_user()

andrey.describe_user()
andrey.greet_user()

den.describe_user()
den.greet_user()
