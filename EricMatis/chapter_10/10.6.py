try:
    first_number = input('Enter the first number: ')
    first_number = int(first_number)
    second_number = input('Enter the second number: ')
    second_number = int(second_number)
except ValueError:
    print("You didn't enter a number!")
else:
    sum = first_number + second_number
    print(f'Sum of numbers: {sum}')
