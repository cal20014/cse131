def get_month():
    is_valid_month = False
    while not is_valid_month:
        month = input("Enter a month number: ")
        is_valid_month, month = validate_month(month) 
    return month

def get_year():
    is_valid_year = False
    while not is_valid_year:
        year = input("Enter a year: ")
        is_valid_year, year = validate_year(year) 
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
    for month in range(1, month):
        total_days += calc_total_days_in_month(month, year)

    return total_days

def calc_total_days(month, year):
    total_days_in_full_years = calc_total_days_in_full_years(year)
    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)

    total_days = total_days_in_full_years + total_days_in_partial_year
    return total_days

def calc_day_of_the_week(total_days):
    day_of_the_week = (total_days + 1) % 7
    return day_of_the_week



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

def num_to_month(month): 
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
    return month_name

def validate_month(month):
    try:
        month = int(month)
        if month < 1 or month > 12:
            print("Invalid entry: month must be between 1 and 12.")
            return False, 0
        else:
            return True, month
    except ValueError:
            print("Invalid entry: month must be an integer.")
            return False, 0
    except TypeError:
            print("Invalid entry: month must be an integer.")
            return False, 0
    
def validate_year(year):
    try:
        year = int(year)
        if year < 1753:
            print("Invalid entry: Year must be 1753 or later.")
            return False, 0
        else:
            return True, year
    except ValueError:
            print("Invalid entry: year must be an integer.")
            return False, 0
    
    except TypeError:
            print("Invalid entry: year must be an integer.")
            return False, 0

def display_calendar(day_of_the_week, total_days_in_month, month, year):

    name_of_month = num_to_month(month)
    print(f"Calendar: {name_of_month} {year}")
    # Display header
    print("Su Mo Tu We Th Fr Sa")

    # If the first day of the month is not monday then add space
    for i in range(day_of_the_week): 
        print("   ", end="")

    for day_of_month in range(1, total_days_in_month + 1):
        print(f"{day_of_month:2} ", end="")

        day_of_the_week += 1
        if day_of_the_week % 7 == 0:
            print()

    if day_of_the_week % 7 != 0:
        print()  

def driver():
    test_cases = [
        [1, 1753],
        [2, 1753],
        [1, 1754],
        [2, 1756],
        [2, 1800],
        [2, 2000],
        ["error", "error"],
        [0, "error"],
        [13, "error"],
        [11, "error"],
        [11, "error"],
        [11, -1],
        [11, 1752],
        [11, 2019],
        ["error", "error"],
        [0, -1],
        [13, 1752],
        [11, 2019]

    ]
    count = 0

    for test_case in test_cases:
        count += 1
        print("====================================")
        print(f"Test case {count}: {test_case}")
        month = test_case[0]
        year = test_case[1]
        is_valid_month, month = validate_month(month)
        is_valid_year, year = validate_year(year)
        if is_valid_month and is_valid_year:
            total_days = calc_total_days(month, year)
            day_of_the_week = calc_day_of_the_week(total_days)
            total_days_in_month = calc_total_days_in_month(month, year)
            print()
            display_calendar(day_of_the_week, total_days_in_month, month, year)
            print()
            day = num_to_day(day_of_the_week)
            print(f"{month}, {year} is a {day}")
            print("====================================\n")

def main():
    """
    
    """
    # Automated testing driver
    driver()

    month = get_month()
    # print(month)

    year = get_year()
    # print(year)

    total_days_in_month = calc_total_days_in_month(month, year)
    # print(total_days_in_month)

    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)
    # print(total_days_in_month)

    total_days_in_full_years = calc_total_days_in_full_years(year)
    # print(total_days_in_full_years)

    total_days = calc_total_days(month, year)
    # print(total_days)

    day_of_the_week = calc_day_of_the_week(total_days)
    # print(day_of_the_week)

    display_calendar(day_of_the_week, total_days_in_month, month, year)

if __name__ == "__main__":
    main()
