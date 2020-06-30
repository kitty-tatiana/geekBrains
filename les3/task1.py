def division(a,b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return print('Неверный ввод')
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return print('Деление на ноль')

first = input('Введите первое число')
second = input('Введите второе число')

print(division(first, second))


