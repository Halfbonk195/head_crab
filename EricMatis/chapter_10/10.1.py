filename = 'learning_python.txt'

with open(filename, encoding="utf-8") as file_object:
    file = file_object.read()
    print(file)

with open(filename, encoding='utf-8') as file_object:
    file = file_object.readlines()
for line in file:
    print(line.rstrip())

with open(filename, encoding='utf-8') as file_object:
    file = file_object.readlines()
my_text = []
for line in file:
    my_text.append(line)

for line in my_text:
    print(line.rstrip())
