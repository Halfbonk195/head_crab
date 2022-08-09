print('The cinema set several ticket prices depending on age.')
while True:
    prompt = 'Do you want to know the ticket price?'
    prompt += '\nHow old are you?\n'
    how_old = input(prompt)
    if how_old == 'quit':
        break

    how_old = int(how_old)
    if how_old < 3:
        print('Ticket is free.')
    elif 3 <= how_old <= 12:
        print('Ticket price $10.')
    else:
        print('Ticket price $15.')
