season = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето',
9:'осень', 10:'осень', 11:'осень', 12:'зима'}

while True:
    month = input('Введите месяц (от 1 до 12)')
    if month.isdigit():
        month = int(month)
        if month > 0 and month <= 12:
            break

print(f'{month} месяц года - это {season.get(month)}')