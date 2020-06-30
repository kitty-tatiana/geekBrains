def my_sum(a, stop):
    ansver = []
    result = 0
    try:
        for i in a:
            ansver.append(int(i))
    except ValueError:
        for i in a:
            if i == 'q':
                stop = False
    for i in ansver:
        result += i
    return result, stop


stop = True
ansver = 0
i = 0
while stop == True:
    user_ansver = input('Введите числа, для остановки нажмите q')
    new_list = user_ansver.split(' ')
    i, stop = my_sum(new_list, stop)
    ansver += i
    print('Сумма чисел равна: ', ansver)
    if stop == False:
        print('Спасибо за внимание')
        break
