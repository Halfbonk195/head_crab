sandwich_orders = ['hamburger', 'panini', 'croque madame and croque monsieur', 'sandwich reuben',
                   'sandwich monte ', 'cristo', 'sandwich dagwood']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

print('\nWe have made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich.title())
