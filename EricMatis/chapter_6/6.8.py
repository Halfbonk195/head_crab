barsik = {'type': 'avcharka', 'master': 'boris'}
lucik = {'type': 'sphinks', 'master': 'jenya'}
musya = {'type': 'none', 'master': 'tanya'}

pets = [barsik, lucik, musya]

for pet in pets:
    for key, value in pet.items():
        print(f'{key.title()}: {value.title()}')
    print()
   