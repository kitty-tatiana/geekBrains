def my_func(x: float, y: int):
    """
    Возвидение числа в степень. Метод 1
    :param x: float
    :param y: int
    :return: int
    """
    c = x ** y
    return c

print(my_func(2, -3))

def my_func2(x: float, y: int):
    """
    Возвидение числа в степень. Метод 2
    :param x: float
    :param y: int
    :return: int
    """
    if y == 0:
        return 1
    else:
        c = x
        degree = abs(y) - 1
        for i in range(degree):
            c = c * x
        if y < 0:
            return 1 / c
        else:
            return c

print(my_func2(2, -3))



