cities = {
    'moscow': {
        'country': 'russia',
        'population': 14000000,
        'fact': 'The year of foundation of Moscow is considered to be 1147, but this is not so. In fact, this is the '
                'year of the first mention of the city in the annals, but the exact year the capital began to exist '
                'is unknown. City Day was first celebrated by residents in 1947, on the 800th anniversary of the '
                'capital. It was then that it was decided that the first Saturday of September would henceforth '
                'become City Day.'
    },
    'yekaterinburg': {
        'country': 'russia',
        'population': 2000000,
        'fact': 'In Soviet times, Yekaterinburg bore the name "Sverdlovsk", but later its former name was returned to '
                'it. '
    },
    'london': {
        'country': 'england',
        'population': 9000000,
        'fact': 'The exact age of London is unknown, but, judging by the chronicles found, it is about two thousand '
                'years old. '
    }
}

for city, info in cities.items():
    print(f'{city.title()}:')
    for key, value in info.items():
        if key == 'country':
            value = value.title()
        print(f'\t{key.title()}: {value}')
    print()
