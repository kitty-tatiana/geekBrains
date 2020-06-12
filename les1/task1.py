date = 12
month = 'июня'
year = 2020

full_date = '{} {} {} года'.format(date, month, year)
print(f'Добрый день!\nСегодня {date} {month} {year} года')
name = input('Как Вас зовут?')
age = int(input('Сколько Вам лет?'))

print('Рады приведствовать! \nДанные о пользователе:\n',name, age, 'лет')