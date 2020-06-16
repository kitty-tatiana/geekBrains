user_list = input('Введите текст')
my_list = user_list.split( )

for ind, word in enumerate(my_list,1):
    i = len(word)
    word_2 = list(word)
    while i > 10:
        word_2.pop(9)
        i = i - 1
        word = ''.join(word_2)
    print(f'{ind} слово Вашего текста: {word}')