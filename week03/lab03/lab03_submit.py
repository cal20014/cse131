"""
This program displays a calendar for a given month and year. It takes into account leap years 
and calculates the correct day of the week for any date after 1753.
"""
# Backlog: Add asserts, Needs a better user interface and options for the user to choose from,

# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      This program displays a calendar for a given month and year.
#      It takes into account leap years and calculates the correct
#      day of the week for any date after 1753.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the calendar table to diplay correctly.
#      I spent hours on this and still couldn't get it to work. I ended up
#      gettting help from Brother Goddridge. He helped me see what I had done wrong.
#      I was able to get the calendar to display correctly after that.
#      I had one extra spance I had to remove. I also inserted more error handling
#      and aligned the test driver code with the main program so that it was
#      correctly testing the program. I also added a few more test cases
#      to be through and make sure I tested all the desired scenarios.
# 5. How long did it take for you to complete the assignment?
#      15 hours

def get_month():
    """
    Prompts the user to enter a month number between 1-12 and validates the input.
    
    Returns:
        int: A valid month number entered by the user.
    """
    is_valid_month = False
    while not is_valid_month:
        month = input("Enter a month number: ")
        is_valid_month, month = validate_month(month) 
    return month

def get_year():
    """
    Prompts the user to enter a year from 1753 or greater and validates the input.
    
    Returns:
        int: A valid year entered by the user.
    """
    is_valid_year = False
    while not is_valid_year:
        year = input("Enter a year: ")
        is_valid_year, year = validate_year(year) 
    return year

def is_leap_year(year):
    """
    Checks if the given year is a leap year.
    
    Parameters:
        year (int): The year to check.
    
    Returns:
        bool: True if the year is a leap year, otherwise False.
    """
    # Years not divisible by 4 are not leap years.
    if year % 4 != 0:
        return False
    # Years divisible by 4 but not by 100 are leap years.
    elif year % 100 != 0:
        return True
    # Years divisible by 100 but not by 400 are not leap years.
    elif year % 400 != 0:
        return False
    else:
        return True

def calc_total_days_in_month(month, year):
    """
    Calculates the total number of days in the specified month and year.
    
    Parameters:
        month (int): The month to check.
        year (int): The year to check.
    
    Returns:
        int: Total number of days in the month for the given year.
    """
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
    """
    Calculates the total number of days from the year 1753 up to, but not including, the given year.
    
    Parameters:
        year (int): The ending year.
    
    Returns:
        int: Total number of days from 1753 up to the given year.
    """
    total_days = 0
    for year in range(1753, year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365

    return total_days

def calc_total_days_in_partial_year(month, year):
    """
    Calculates the total number of days from January up to, but not including, the given month in the given year.
    
    Parameters:
        month (int): The ending month.
        year (int): The year to check.
    
    Returns:
        int: Total number of days from January up to the given month in the given year.
    """
    total_days = 0
    for month in range(1, month):
        total_days += calc_total_days_in_month(month, year)

    return total_days

def calc_total_days(month, year):
    """
    Calculates the total number of days from 1753 up to the given month and year.
    
    Parameters:
        month (int): The month to check.
        year (int): The year to check.
    
    Returns:
        int: Total number of days from 1753 up to the given month and year.
    """
    # Calculates total days in full years from 1753 up to the given year.
    total_days_in_full_years = calc_total_days_in_full_years(year)
    # Calculates total days in the given year up to the given month.
    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)
    # Sum of both calculations gives the total number of days from 1753 up to the given month and year.
    total_days = total_days_in_full_years + total_days_in_partial_year
    return total_days

def calc_day_of_the_week(total_days):
    """
    Calculates the day of the week for a given total number of days since 1753.
    
    Parameters:
        total_days (int): Total number of days since 1753.
    
    Returns:
        int: A number representing the day of the week (0 for Sunday, 1 for Monday, ...).
    """
    day_of_the_week = (total_days + 1) % 7
    return day_of_the_week

def num_to_day(day_of_the_week):
    """
    Converts a number to its corresponding day of the week name.
    
    Parameters:
        day_of_the_week (int): Number representing the day of the week.
    
    Returns:
        str: The name of the day of the week.
    """
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
    """
    Converts a month number to its corresponding month name.
    
    Parameters:
        month (int): Month number.
    
    Returns:
        str: The name of the month.
    """
# Converts month number to month name.
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
    """
    Validates if the provided month is a valid number between 1-12.
    
    Parameters:
        month (str -> int): Month to validate.
    
    Returns:
        - True and the month number if valid, otherwise False and 0.
    """
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
    """
    Validates if the provided year is valid is equal to 1753 or greater.
    
    Parameters:
        year (str -> int): Year to validate.
    
    Returns:
        - True and the year if valid, otherwise False and 0.
    """
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
    """
    Displays a calendar for the given month and year.
    
    Parameters:
        day_of_the_week (int): The day of the week for the first day of the month.
        total_days_in_month (int): Total number of days in the month.
        month (int): Month number.
        year (int): Year number.
    """

    name_of_month = num_to_month(month)
    print(f"Calendar: {name_of_month} {year}")
    # Display header.
    print("Su Mo Tu We Th Fr Sa")

    # Add space until we reach the first day of the month.
    for i in range(day_of_the_week): 
        print("   ", end="")

    for day_of_month in range(1, total_days_in_month + 1):
        print(f"{day_of_month:2} ", end="")

        day_of_the_week += 1
        # Start a new line after every week (every 7 days).
        if day_of_the_week % 7 == 0:
            print()

    if day_of_the_week % 7 != 0:
        print()  

def driver():
    """
    Automated test driver to validate various functions of the program.
    Displays the calendar for the given month and year for each test case.
    """
    # A two dimensional array of test cases to test the desired outcomes.
    # Each test case consists of a month and a year value. 
    # Month on the left. Year on the right.
    test_cases = [
        [1, 1753],     # Start of the calendar system
        [2, 1753],     # Second month of the start year
        [1, 1754],     # Non-leap year
        [2, 1756],     # Leap year
        [2, 1800],     # Century year, not a leap year
        [2, 2000],     # Century year that is a leap year
        ["error", "error"],   # Invalid input: non-integer values
        [0, "error"],  # Month is less than 1
        [13, "error"], # Month is more than 12
        [11, "error"], 
        [11, "error"], 
        [11, -1],      # Valid month, invalid year. Year is less than 1753
        [11, 1752],    # Year just before the start of the calendar system in 1753
        [11, 2019],    
        ["error", "error"],   # Invalid input: non-integer values (repeated intentionally for demonstration)
        [0, -1],       # Month is less than 1, year is less than 1753
        [13, 1752],    # Month is more that 12, year is less than 1753
        [11, 2019]     
    ]
    count = 0
    # Loops through each test case in the array.
    for test_case in test_cases: # Add asserts for the for loop
        count += 1
        print("====================================")
        print(f"Test case {count}: {test_case}")
        month = test_case[0]
        year = test_case[1]

        # Validate month and year inputs
        is_valid_month, month = validate_month(month)
        is_valid_year, year = validate_year(year)

        # If both the month and year are valid,
        # proceed to calculate and display the calendar
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
    Main function that drives the program. It prompts the user for month and year, calculates the calendar, 
    and displays it.
    """
    DEBUG = False  # Set this to False when you don't want debug outputs to be displayed.

    # Automated testing driver
    driver()

    month = get_month()
    if DEBUG:
        print(month)

    year = get_year()
    if DEBUG:
        print(year)

    total_days_in_month = calc_total_days_in_month(month, year)
    if DEBUG:
        print(total_days_in_month)

    total_days_in_partial_year = calc_total_days_in_partial_year(month, year)
    if DEBUG:
        print(total_days_in_month)

    total_days_in_full_years = calc_total_days_in_full_years(year)
    if DEBUG:
        print(total_days_in_full_years)

    total_days = calc_total_days(month, year)
    if DEBUG:
        print(total_days)

    day_of_the_week = calc_day_of_the_week(total_days)
    if DEBUG:
        print(day_of_the_week)

    display_calendar(day_of_the_week, total_days_in_month, month, year)

if __name__ == "__main__":
    main()