def int_func(text):
    text = text[0].upper() + text[1:]
    return text

user_ansver = str(input('Введите слово'))
print(int_func(user_ansver))
user_ansver = str(input('Введите текст'))
new_list = user_ansver.split(' ')
print(new_list)
ansver = []
for i in new_list:
    ansver.append(int_func(i))
print(' '.join(ansver))