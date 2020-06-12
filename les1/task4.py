while True:
    ansver = input('Введите челое положительное число')
    if ansver.isdigit():
        ansver = int(ansver)
        if ansver > 0:#
            break

print(f'Найбольшая цифра в числе {ansver} равна')
max_number = ansver % 10
while ansver > 0:
    i = ansver % 10
    if i > max_number:
        max_number = i
    ansver = ansver // 10

print(max_number)
