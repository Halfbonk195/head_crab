from random import randint

iteration = 0
continue_game = True
answers = ['да', 'ДА', 'Да', 'Yes', 'yes', 'YES']
print('Программа загадывает число от 1 до N')

while continue_game:
    N = int(input('Введите число N: '))
    answer_number = randint(1, N + 1)

    while True:
        iteration += 1
        print(f'\nПопытка №{iteration}')

        in_number = int(input('Введите предполагаемое число: '))

        if in_number > answer_number:
            print(f'Загаданное число меньше, чем {in_number}')
        elif in_number < answer_number:
            print(f'Загаданное число больше, чем {in_number}')
        else:
            print(f'Вы отгадали число {in_number} c {iteration} попытки!')
            break
    answer = input('Введите "да" для повторения игры: ')
    if answer not in answers:
        continue_game = False
