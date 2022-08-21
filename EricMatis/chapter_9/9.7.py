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

        print(f'Hello, {self.first_name} {self.last_name}! We were waiting for you.')
        print('----------------------------------------------')

    def increment_login_attempts(self):
        """Суммирует количество попыток входа"""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество поптыток входа"""

        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, e_mail, age, login):
        super().__init__(first_name, last_name, e_mail, age, login)
        self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей',
                           'разрешено управлять пользователями', 'разрешено добавлять пользователей']

    def show_privileges(self):
        """Выводит привилегии администратора"""

        print(f'Пользователь {self.first_name} {self.last_name} имеет следующие привилегии:')
        for privilege in self.privileges:
            print(f'{privilege.title()}')


user_admin = Admin('тимофей', 'антипин', 'halfbonk@mail.ru', 28, 'halfbonk')
user_admin.greet_user()
user_admin.describe_user()
user_admin.show_privileges()
