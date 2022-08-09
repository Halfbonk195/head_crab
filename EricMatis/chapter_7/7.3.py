number = input('Enter your number and we will see if it is a multiple of 10: ')
number = int(number)
if number % 10 == 0:
    print(f'The number {number} is a multiple of 10!')
else:
    print(f'The number {number} is not a multiple of 10...')
