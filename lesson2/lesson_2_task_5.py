def month_to_season(x):
    if x == 1 or x == 2 or x == 12:
        return ("Зима")
    elif x == 3 or x == 4 or x == 5:
        return ("Весна")
    elif x == 6 or x == 7 or x == 8:
        return ("Лето")
    elif x == 9 or x == 10 or x == 11:
        return ("Осень")
    else:
        return ("Укажите правильный номер месяца:")
print(month_to_season(int(input("Введите номер месяца:"))))