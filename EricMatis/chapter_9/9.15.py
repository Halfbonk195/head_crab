from random import choice

my_list = [1234, 5432, 1111, 6465, 9262, 7234, 3999, 8090, 2222, 2415, 5321, 2000, 8992, 1826, 4930]

iteration = 1
while True:
    ticket = choice(my_list)
    if ticket == 1234:
        print(f'Это {iteration}-я итерация')
        print(f'Вы победили! Выпало число {ticket}!')
        break
    iteration += 1
