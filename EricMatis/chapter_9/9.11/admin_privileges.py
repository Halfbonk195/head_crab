from user import User

"""Привилегии для админа и админ"""


class Privileges:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей',
                           'разрешено управлять пользователями', 'разрешено добавлять пользователей']

    def show_privileges(self):
        """Выводит привилегии пользователя"""

        print(f'Пользователь {self.first_name} {self.last_name} имеет следующие привилегии:')
        for privilege in self.privileges:
            print(f'{privilege.title()}')


class Admin(User):

    def __init__(self, first_name, last_name, e_mail, age, login):
        super().__init__(first_name, last_name, e_mail, age, login)
        self.privileges = Privileges(self.first_name, self.last_name)
