"""Простая модель ресторана"""


class Restaurant:
    """Класс ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит описание ресторана"""

        print(f'Restaurant name is {self.restaurant_name}. There is an {self.cuisine_type} kitchen')

    def open_restaurant(self):
        """Открывает ресторан"""

        print(f'Restaurant {self.restaurant_name} is open!')

    def close_restaurant(self):
        """Закрывает ресторан"""

        print(f'Restaurant {self.restaurant_name} is close!')

    def set_number_served(self, number):
        """Устанавливает количество посетителей за месяц на начало следующего дня"""

        if number >= self.number_served:
            self.number_served = number
        else:
            print(f"You can't reduce the number of visitors")

    def increment_number_served(self, number):
        """Учитывает количество новых посетителей"""

        self.number_served += number
