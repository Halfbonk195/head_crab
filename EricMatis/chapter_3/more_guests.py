guests = ['afony', 'kapitoly', 'alexandr', 'wasserman']
guests[0] = 'andron'

print('Оказывается стол может вместить еще 3 гостей.')
guests.insert(0, 'brandan')
guests.insert(3, 'vasily')
guests.append('begemot')
print(f'Я приглашаю тебя {guests[0].title()} в гости!')
print(f'Я приглашаю тебя {guests[1].title()} в гости!')
print(f'Я приглашаю тебя {guests[2].title()} в гости!')
print(f'Я приглашаю тебя {guests[3].title()} в гости!')
print(f'Я приглашаю тебя {guests[4].title()} в гости!')
print(f'Я приглашаю тебя {guests[5].title()} в гости!')
print(f'Я приглашаю тебя {guests[6].title()} в гости!\n')
print(f'Количество госетй: {len(guests)}')
print('Новый обеденный стол не успеют привезти и места хватит только для 2-х гостей.')
deleted_guest = guests.pop()
print(f'Я сожалею об отмене приглашения {deleted_guest}')
deleted_guest = guests.pop()
print(f'Я сожалею об отмене приглашения {deleted_guest}')
deleted_guest = guests.pop()
print(f'Я сожалею об отмене приглашения {deleted_guest}')
deleted_guest = guests.pop()
print(f'Я сожалею об отмене приглашения {deleted_guest}')
deleted_guest = guests.pop()
print(f'Я сожалею об отмене приглашения {deleted_guest}')

print(f'Я приглашаю тебя {guests[0].title()} в гости!')
print(f'Я приглашаю тебя {guests[1].title()} в гости!')

del guests[0]
del guests[0]
print(guests)
