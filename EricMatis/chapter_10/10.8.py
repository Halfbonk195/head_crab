def reading_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        f_strings = f.readlines()
    print(f"Read file '{file_name}':")
    for string in f_strings:
        print(string.rstrip())
    print()


my_files = ['cats.txt', 'dogs.txt', 'my_python.txt']

for file in my_files:
    try:
        reading_file(file)
    except FileNotFoundError:
        print(f"No such file '{file}'!")
