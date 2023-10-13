def get_month():
    while True:
        month = int(input("Enter a month number: "))
        if month == type(int) == False:
            print("Invalid entry: Month must be an integer.")
        elif month < 1 or month > 12:
            print("Invalid entry: Month must be between 1 and 12.")
        else:
            return month


def get_year():
    while True:
        year = int(input("Enter a year: "))
        if year == type(int) == False:
            print("Invalid entry: Year must be an integer.")
        elif year < 1753:
            print("Invalid entry: Year must be 1753 or later.")
        else:
            return year


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def calc_total_days_in_month(month, year):
    match month:
        case 1, 3, 5, 7, 8, 10, 12:
            return 31
        case 4, 6, 9, 11:
            return 30
        case 2:
            leap_year = is_leap_year(year)
            if leap_year == False:
                return 28
            else:
                return 29


def calc_total_days(month, year):
    total_days_in_full_years = calc_total_days_in_full_years()
    total_days_in_partial_year = calc_total_days_in_partial_year()

    total_days = total_days_in_full_years + total_days_in_partial_year
    return total_days


def calc_total_days_in_full_years(year):
    pass


def calc_total_days_in_partial_year(month, year):
    total_days = 0
    for month in range(1, month):
        total_days_in_month = calc_total_days_in_month(month, year)
        total_days += total_days_in_month

    return total_days


def main():
    month = get_month()
    year = get_year()
    total_days_in_month = calc_total_days_in_month(month, year)
    total_days = calc_total_days_in_partial_year(month, year)
    print(total_days)


if __name__ == "__main__":
    main()
