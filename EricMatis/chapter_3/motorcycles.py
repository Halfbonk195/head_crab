motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

popped_motorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycles.title())

motorcycles = ['honda', 'yamaha', 'suzuki', 'motor', 'suzuki']
print()
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
