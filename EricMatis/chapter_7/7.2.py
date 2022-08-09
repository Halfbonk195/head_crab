table_size = input('For how many people do you want to book a table? ')
table_size = int(table_size)
if table_size > 8:
    print('Unfortunately, you will have to wait.')
else:
    print('The table is ready.')
