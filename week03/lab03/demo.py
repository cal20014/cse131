def get_month():
    while True:
        try:
            month = int(input("Enter a month number: "))
            if month < 1 or month > 12:
                print("Invalid entry: Month must be between 1 and 12.")
            else:
                return month
        except ValueError:
            print("Invalid entry: Month must be an integer.")


def get_year():
    while True:
        try:
            year = int(input("Enter a year: "))
            if year < 1753:
                print("Invalid entry: Year must be 1753 or later.")
            else:
                return year
        except ValueError:
            print("Invalid entry: Year must be an integer.")


def calc_total_days_in_full_years(year):
    total_days = 0
    for y in range(1753, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    return total_days


def calc_total_days_in_partial_year(month, year):
    total_days = 0
    for m in range(1, month + 1):
        total_days += calc_total_days_in_month(m, year)

    return total_days


def display_calendar(day_of_the_week, total_days_in_month, month, year):
    # Table header
    print(f"\nCalendar for {month} {year}")
    print("Su Mo Tu We Th Fr Sa")

    # Display leading spaces
    for i in range(day_of_the_week):
        print("   ", end="")  # Display three spaces

    # Display each day in the month
    for day_of_month in range(1, total_days_in_month + 1):
        print(
            f"{day_of_month:2} ", end=""
        )  # Display day of the month with space padding
        day_of_the_week += 1
        if day_of_the_week % 7 == 0:
            print()  # Newline

    # Check if we need an additional newline at the end
    if day_of_the_week % 7 != 0:
        print()  # Newline


def main():
    month = get_month()
    year = get_year()
    total_days_in_month = calc_total_days_in_month(month, year)
    total_days = calc_total_days(month, year)
    dow = calc_day_of_the_week(
        total_days - total_days_in_month + 1
    )  # Adjusting to get the correct starting day
    display_calendar(dow, total_days_in_month, month, year)


# I'm just defining the main function here.
# To run it interactively, you can call main() after this cell is executed.
main
