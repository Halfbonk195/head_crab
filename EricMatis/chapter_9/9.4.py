class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}. There is an {self.cuisine_type} kitchen')

    def open_restaurant(self):
        print('Restaurant is open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('Svoya Kompania', 'Open')
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(56)
print(restaurant.number_served)

restaurant.describe_restaurant()
