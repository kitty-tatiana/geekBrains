while True:
    time = input('Введите время в секундах')
    if time.isdigit():
        time = int(time)
        break

print(time, 'секунд это:')
hour = time // 3600
time = time % 3600
minutes = time // 60
sec = time % 60

print (f'{hour:>02}:{minutes:>02}:{sec:>02}')


