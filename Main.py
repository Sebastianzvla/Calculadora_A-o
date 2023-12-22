def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(Year, N):
    x = is_leap(Year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x == True and N == 2:
        return 29
    return month_days[N - 1]

year = int(input("Año (ej. 2001, 1948): ")) 
month = int(input("Mes (ej. 2, 11): "))
days = days_in_month(year, month)
print(days)

