my_list = [6, 6, 5, 4, 4, 2, 1]

print(my_list)
print(' ')
for i in range(4):
    while True:
        ansver = input('Введите число от 0 до 9')
        if ansver.isdigit():
            ansver = int(ansver)
            if ansver >= 0 and ansver <= 10:
                break
    if my_list[0] < ansver:
        my_list.insert(0, ansver)
    if ansver == 0:
        my_list.append(ansver)
    if my_list.count(ansver) == 0:
        for ind, itm in enumerate(my_list):
            if itm < ansver:
                my_list.insert(ind, ansver)
                break
    else:
        pos = my_list.index(ansver)
        num = my_list.count(ansver)
        my_list.insert(pos + num, ansver)

    print(my_list)

