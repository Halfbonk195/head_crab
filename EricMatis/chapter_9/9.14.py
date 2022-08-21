from random import choice

my_list = [123, 5432, 1, 465, 262, 73234, 398999, 80890, 2222, 215, 5321, 2]

print('Следующие номера являются выигрышными:')
for fee in range(4):
    print(f'{choice(my_list)}')
