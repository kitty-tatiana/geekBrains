while True:
    length = input('Введите длину списка')
    if length.isdigit():
        length = int(length)
        break

user_list = []
for i in range(length):
    user_list.append(input(f'Введите {i + 1} елемент строки'))

print(user_list)

if length % 2 ==0:
    for i in range(0, length, 2):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
else:
    for i in range(0, length - 1, 2):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(user_list)
