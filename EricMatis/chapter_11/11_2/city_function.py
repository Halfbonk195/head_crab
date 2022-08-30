def get_city_country(city, country, population=''):
    """Строит отформатированную строку вида 'Город, Страна'"""
    full_string = f'{city}, {country}'
    full_string = full_string.title()
    if population:
        full_string += f' - population {population}'
    return full_string
