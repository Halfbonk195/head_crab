my_dict = {
    'строки': 'представляет собой простую последовательность символов',
    'числа': 'в Python два вида чисел - целые и вещественные',
    'комментарии': 'позволяют описывать общий подход к решаемой задаче',
    'списки': 'представляет собой набор элементов, следующих в определенном порядке',
    'генератор_списка': 'позволяет сгенерировать список в одной строке',
    'кортежи': 'неизменяемые списки',
    'if': 'условный оператор',
}

print(f"Строки:\n\t{my_dict['строки'].capitalize()}.\n"
      f"Числа:\n\t{my_dict['числа'].capitalize()}.\n"
      f"Комментарии:\n\t{my_dict['комментарии'].capitalize()}.\n"
      f"Списки:\n\t{my_dict['списки'].capitalize()}.\n"
      f"Генератор списка:\n\t{my_dict['генератор_списка'].capitalize()}.\n"
      f"Кортежи:\n\t{my_dict['кортежи'].capitalize()}")

for key in my_dict:
    print(key)
print(my_dict.keys())
