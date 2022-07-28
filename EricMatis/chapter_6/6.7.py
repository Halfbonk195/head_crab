man_1 = {'first_name': 'timofey', 'last_name': 'antipin', 'age': 28, 'city': 'yekaterinburg'}
man_2 = {'first_name': 'andrey', 'last_name': 'marcinkovski', 'age': 36, 'city': 'moscow'}
man_3 = {'first_name': 'boris', 'last_name': 'bochovski', 'age': 17, 'city': 'new york'}

people = [man_1, man_2, man_3]
for person in people:
    print(f"First name: {person['first_name'].title()}\nLast name: {person['last_name'].title()}")
    print(f"Age: {person['age']}\nCity: {person['city'].title()}\n")
