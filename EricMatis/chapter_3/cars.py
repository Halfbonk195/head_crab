cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Временная сортировка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

print('\nHere is the sorted revers list:')
print(sorted(cars, reverse=True))

# Метод reverse

print(f'\n{cars}')

cars.reverse()
print(f'\n{cars}')

print('\nДлина списка')
print(len(cars))
