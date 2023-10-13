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
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        leap_year = is_leap_year(year)
        return 29 if leap_year else 28
    else:
        print("Invalid month")


def calc_total_days_in_full_years(year):
    total_days = 0
    for year in range(1753, year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365

    return total_days


def calc_total_days_in_partial_year(month, year):
    total_days = 0
    for month in range(1, month + 1):
        total_days += calc_total_days_in_month(month, year)

    return total_days


def calc_total_days(month, year):
    total_days_in_full_years = calc_total_days_in_full_years(year)
    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)

    total_days = total_days_in_full_years + total_days_in_partial_year
    return total_days


def calc_day_of_the_week(total_days):
    day_of_the_week = total_days % 7
    return day_of_the_week


# def display_calendar(day_of_the_week, total_days_in_month, month, year):
#     print(f"Calendar for {month} {year}")
#     print("Su Mo Tu We Th Fr Sa")
#     print("--------------------")
#     print("  " * day_of_the_week, end="")
#     for day in range(1, total_days_in_month + 1):
#         print(f"{day:2d} ", end="")
#         if calc_day_of_the_week(day) == 6:
#             print()


def display_calendar(day_of_the_week, total_days_in_month):
    # Table header
    print("SU MO TU WE TH FR SA")
    # Display leading spaces
    for i in range(0, day_of_the_week):
        print("    ")  # Display four spaces

    # Display each day in the month
    for day_of_month in range(1, total_days_in_month):
        print(f"{day_of_month}")  # Display day of the month with space padding
        print(day_of_month)

        day_of_the_week += 1
        if day_of_the_week % 7 == 0:
            print()  # Newline

        if day_of_the_week % 7 != 0:
            print()  # Newline


def main():
    month = get_month()
    print(month)

    year = get_year()
    print(year)

    total_days_in_month = calc_total_days_in_month(month, year)
    print(total_days_in_month)

    total_days_in_month = calc_total_days_in_partial_year(month, year)
    print(total_days_in_month)

    total_days_in_full_years = calc_total_days_in_full_years(year)
    print(total_days_in_full_years)

    total_days = calc_total_days(month, year)
    print(total_days)

    day_of_th_week = calc_day_of_the_week(total_days)
    print(day_of_th_week)

    display_calendar(day_of_th_week, total_days_in_month)


if __name__ == "__main__":
    main()
