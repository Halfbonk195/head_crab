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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['milk ice cream', 'creme brulee', 'Melorin', 'Sherbet', 'Popsicles', 'Italian ice', 'Granita']

    def print_flavors(self):
        """Выводит список доступных видов мороженного"""

        print(f'The following types of ice cream are available:')
        for ice_cream in self.flavors:
            print(ice_cream.title())


ice_cream_restaurant = IceCreamStand('Capitol', 'Ice cream')
ice_cream_restaurant.open_restaurant()
ice_cream_restaurant.set_number_served(5609)
ice_cream_restaurant.print_flavors()

ice_cream_restaurant.close_restaurant()
