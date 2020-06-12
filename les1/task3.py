number1 = input('Введите число')
total = int(number1)
number2 = number1 + number1
total = total +int(number2)
number3 = number2 + number1
total = total + int(number3)
print(f'Сумма чисел {number1}+{number2}+{number3} =',total)