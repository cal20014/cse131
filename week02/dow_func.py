def calc_dow(total_days):
    dow = total_days % 7
    name_of_day = ""

    if dow == 1:
        name_of_day = "Monday"
    elif dow == 2:
        name_of_day = "Tuesday"
    elif dow == 3:
        name_of_day = "Wednesday"
    elif dow == 4:
        name_of_day = "Thursday"
    elif dow == 5:
        name_of_day = "Friday"
    elif dow == 6:
        name_of_day = "Saturday"
    elif dow == 7:
        name_of_day = "Sunday"
    else:
        print("Error: Invalid day number.")

    return name_of_day


def main():
    total_days = 13
    day = calc_dow(total_days)
    print(day)
    print(calc_dow(total_days + 2))


if __name__ == "__main__":
    main()
