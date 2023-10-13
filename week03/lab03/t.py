def display_table(num_days, dow):
    # Print table header
    header = "SU MO TU WE TH FR SA"
    print(header)

    # Print leading spaces based on the day of the week (dow)
    for _ in range(dow):
        print("    ", end="")

    # Print the days of the month
    for dom in range(1, num_days + 1):
        print(f"{dom:2}", end=" ")

        # Update the day of the week (dow) and print newline if it's Sunday (dow % 7 == 0)
        dow += 1
        if dow % 7 == 0:
            print()

    # Print newline if the last row isn't complete (dow % 7 != 0)
    if dow % 7 != 0:
        print()


# Example usage:
num_days = 31  # Replace with the number of days in the month you want to display
dow = 0  # Replace with the day of the week (0 for Sunday, 1 for Monday, etc.)
display_table(num_days, dow)
