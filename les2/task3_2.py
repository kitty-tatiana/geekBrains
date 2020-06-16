season = {'зима': (12, 1, 2),
          'весна': (4, 5, 3),
          'лето': (6, 7, 8),
          'осень': (9, 10, 11)}

while True:
    month = input('Введите месяц (от 1 до 12)')
    if month.isdigit():
        month = int(month)
        if month > 0 and month <= 12:
            break

for key, itm in season.items():
    if month in itm:
        print(f'{month} месяц года - это {key}')