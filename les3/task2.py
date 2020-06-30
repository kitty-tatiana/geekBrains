def info(name, surname, b_year, city, email, phone):
    """
    Функция выводит данные о пользователе
    :param name: str
    :param surname: str
    :param b_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    """
    return print(f'Имя:{name}; Фамилия:{surname}; год рождения:{b_year}; город проживания:{city}; контактные данные {email}, {phone}')


info(name = 'Петя', surname = 'Васичкин', b_year = 1968 , city = 'Киев', email = '23@gmail.com', phone = 102)