while True:
    revenue = input('Введите выручку компании')
    if revenue.isdigit():
        revenue = int(revenue)
        break

while True:
    costs = input('Введите издержки компании')
    if costs.isdigit():
        costs = int(costs)
        break

if revenue > costs:
    print(f'Фирма приносит прибыль. Рентабельность выручки: {revenue/costs:.2f}')#
    while True:
        workers = input('Какое количество сотрудников работает на Вашей фирме?')
        if workers.isdigit():
            workers = int(workers)
            break
    print(f'Прибыль фирмы с расчетом на одного сотрудника равна: {(revenue - costs)/workers:.2f}')
else:
    print('Ваша фирма работает в обыток')
