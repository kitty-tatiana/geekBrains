while True:
    month = input('Введите месяц (от 1 до 12)')
    if month.isdigit():
        month = int(month)
        if month > 0 and month <= 12:
            break

season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень',
          'осень', 'осень', 'зима']
print(f'{month} месяц года - это {season[month - 1]}')