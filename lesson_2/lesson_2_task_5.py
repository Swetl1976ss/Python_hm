def month_to_season(month):

    if month == 12 or month < 3:
        return 'Зима'
    elif month >= 3 and month < 6:
        return 'Весна'
    elif month >= 6 and month < 9:
        return 'Лето'
    else:
        return ' Осень'


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")