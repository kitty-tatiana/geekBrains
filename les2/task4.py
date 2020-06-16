user_list = input('Введите текст')
my_list = user_list.split( )

for ind, word in enumerate(my_list,1):
    print(f'{ind} слово Вашего текста: {word[:10]}')