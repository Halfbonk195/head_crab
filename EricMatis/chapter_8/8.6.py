def city_country(city, country):
    message = f'{city.title()}, {country.title()}'
    return message


text = city_country('Yekaterinburg', 'russia')
print(text)

text = city_country('london', 'england')
print(text)

text = city_country('paris', 'french')
print(text)
