file_name = 'the_best_python.txt'

with open(file_name, 'a') as file_object:
    print("For quit press 'q'")
    while True:
        answer = input('Write one reason why you like programming in python: ')
        if answer == 'q':
            break
        file_object.write(answer + '\n')
