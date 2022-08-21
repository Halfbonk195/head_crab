class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}. There is an {self.cuisine_type} kitchen')

    def open_restaurant(self):
        print('Restaurant is open!')


restaurant_1 = Restaurant('Svoya Kompania', 'Open')
restaurant_2 = Restaurant('Bykovski', 'Close')
restaurant_3 = Restaurant('BK', 'Open')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
