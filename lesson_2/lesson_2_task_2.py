year = int(input("Введите год:"))


def is_year_leap(year):

    if year % 4 == 0:
        n = 'Trye'
    else:

        n = 'False'

    print(year, n)


is_year_leap(year)