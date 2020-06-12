while True:
    start_km = input('Сколько киллометров пробежал спортсмен в первый день?')
    if start_km.isdigit():
        start_km = int(start_km)
        break

while True:
    finish_km = input('Какого результата хочет добится спортсмен?')
    if finish_km.isdigit():
        finish_km = int(finish_km)
        break

i = 1
while start_km < finish_km:
    print(f'{i}-й день: {start_km:.2f}')
    start_km = start_km * 1.1
    i = i + 1
print(f'{i}-й день: {start_km:.2f}')
print(f'Ответ: на {i}-тый день спортсмен достиг результата не менее {finish_km} км.')
