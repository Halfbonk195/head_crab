sandwich_orders = ['hamburger', 'panini', 'pastrami', 'croque madame and croque monsieur', 'pastrami',
                   'sandwich reuben', 'pastrami', 'sandwich monte cristo', 'pastrami', 'sandwich dagwood']
finished_sandwiches = []

print('No more pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

print('\nWe have made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich.title())
