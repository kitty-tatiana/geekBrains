def my_func(a, b, c):
    return max(a + b, a + c, b + c)

user_ansver1 =int(input('Введите 1 значения '))
user_ansver2 =int(input('Введите 2 значения '))
user_ansver3 =int(input('Введите 3 значения '))
print(my_func(user_ansver1, user_ansver2, user_ansver3))