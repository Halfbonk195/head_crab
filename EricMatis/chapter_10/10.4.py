file_name = 'guest.txt'

with open(file_name, 'a') as file_object:
    print('For quit press q')
    while True:
        name_guest = input('Please, enter your name: ')
        if name_guest == 'q':
            break
        print(f'Greetings, {name_guest.title()}!')
        file_object.write(name_guest + '\n')
       