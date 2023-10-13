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
    try:
        while True:
            year = int(input("Enter a year: "))
            if year < 1753:
                print("Invalid entry: Year must be 1753 or later.")
            else:
                return year
    except ValueError:
        print("Invalid entry: Month must be an integer.")


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
    for month in range(1, month):
        total_days += calc_total_days_in_month(month, year)

    return total_days


def calc_total_days(month, year):
    total_days_in_full_years = calc_total_days_in_full_years(year)
    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)

    total_days = total_days_in_full_years + total_days_in_partial_year
    return total_days


def calc_day_of_the_week(total_days):
    day_of_the_week = total_days % 7
    return day_of_the_week + 1


# def display_calendar(day_of_the_week, total_days_in_month, month, year):
#     print(f"Calendar for {month} {year}")
#     print("Su Mo Tu We Th Fr Sa")
#     print("--------------------")
#     print("  " * day_of_the_week, end="")
#     for day in range(1, total_days_in_month + 1):
#         print(f"{day:2d} ", end="")
#         if calc_day_of_the_week(day) == 6:
#             print()


def display_calendar(day_of_the_week, total_days_in_month, month, year):
    # Convert month number to month name
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month_name = month_names[month - 1]

    # Table header
    print(f"Calendar for {month_name} {year}")
    print("Su Mo Tu We Th Fr Sa")

    # Display leading spaces
    for i in range(0, day_of_the_week):
        print("    ", end="")  # Display four spaces

    # Display each day in the month
    for day_of_month in range(1, total_days_in_month + 1):
        print(f"{day_of_month:2} ", end="")  # Display day of the month with space padding

        day_of_the_week += 1
        if day_of_the_week % 7 == 0:  # If it's the end of the week, print newline
            print()

    if day_of_the_week % 7 != 0:  # Print newline if the last day is not a Saturday
        print()

def num_to_day(day_of_the_week):
    if day_of_the_week == 0:
        return "Sunday"
    elif day_of_the_week == 1:
        return "Monday"
    elif day_of_the_week == 2:
        return "Tuesday"
    elif day_of_the_week == 3:
        return "Wednesday"
    elif day_of_the_week == 4:
        return "Thursday"
    elif day_of_the_week == 5:
        return "Friday"
    elif day_of_the_week == 6:
        return "Saturday"
    else:
        return "Error: Invalid day number."

def validate_date(date):
    try:
        if date < 1 or date > 12:
            print("Invalid entry: date must be between 1 and 12.")
        else:
            return date
    except ValueError:
            print("Invalid entry: date must be an integer.")



def driver():
    test_cases = [
        [1, 1753],
        [2, 1753],
        [1, 1754],
        [2, 1756],
        [2, 1800],
        [2, 2000],
        # ["error", "error"]
        # [0, -1]
        # [13, 1752]
        # [11, 2019]
    ]
    count = 0

    for test_case in test_cases:
        print("====================================")
        print(f"Test case {count}: {test_case}")
        month = test_case[0]
        year = test_case[1]
        validate_date(month)
        validate_date(year)
        total_days = calc_total_days(month, year)
        day_of_the_week = calc_day_of_the_week(total_days)
        total_days_in_month = calc_total_days_in_month(month, year)
        display_calendar(day_of_the_week, total_days_in_month, month, year)
        print("====================================")


        day = num_to_day(day_of_the_week)
        print(f"{month}, {year} is a {day}")
        count += 1

def main():
    # automated testing
    driver()

    month = get_month()
    print(month)

    year = get_year()
    print(year)

    total_days_in_month = calc_total_days_in_month(month, year)
    print(total_days_in_month)

    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)
    print(total_days_in_month)

    total_days_in_full_years = calc_total_days_in_full_years(year)
    print(total_days_in_full_years)

    total_days = calc_total_days(month, year)
    print(total_days)

    day_of_the_week = calc_day_of_the_week(total_days)
    print(day_of_the_week)

    display_calendar(day_of_the_week, total_days_in_month, month, year)



if __name__ == "__main__":
    main()
