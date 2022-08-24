file_name = 'learning_python.txt'

with open(file_name, encoding='utf-8') as file_object:
    my_text = file_object.readlines()
    for line in my_text:
        line_c = line.replace('Python', 'C')
        print(line_c.rstrip())
