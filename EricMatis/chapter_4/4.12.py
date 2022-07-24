my_foods = ['pizza', 'falafel', 'carrot cake', 'potato', 'makaroni', 'cake']
print('The first three items in the list are:')
for food in my_foods[:3]:
    print(food)

print('Three items from the middle of the list are:')
for food in my_foods[2:5]:
    print(food)

print('The last three items in the list are:')
for food in my_foods[-3:]:
    print(food)
