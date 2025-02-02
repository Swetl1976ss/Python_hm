import math


def square(n):

    n = float(input('Введите длину стороны квадрата'))
    S = math.ceil(n ** 2)
    return 'Длина стороны =: ', n, 'Площадь квадрата',  S


print(square('n'))
