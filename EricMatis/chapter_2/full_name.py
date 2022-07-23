first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

# f-strings
print(f'Hello, {full_name.title()}!')

message = f'Hello, {full_name.title()}!'
print(message)

# Символы табуляции и новой строки
print('\tPython')
print('Languages:\nPython\nC\nJavaScript')
print('Languages:\n\tPython\n\tC\n\tJavaScript')

# Удаление пропусков
favorite_language = 'python '
print(favorite_language + 'end')

favorite_language = favorite_language.rstrip()
print(favorite_language + 'end')

favorite_language = ' python'
print(favorite_language)

favorite_language = favorite_language.lstrip()
print(favorite_language)
