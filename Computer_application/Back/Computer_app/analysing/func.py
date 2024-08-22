def leap_year(year):
    year = int(year)
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        return True
    return False
