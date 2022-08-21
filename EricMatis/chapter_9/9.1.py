class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}. There is an {self.cuisine_type} kitchen')

    def open_restaurant(self):
        print('Restaurant is open!')


restaurant = Restaurant('Svoya Kompania', 'Open')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
