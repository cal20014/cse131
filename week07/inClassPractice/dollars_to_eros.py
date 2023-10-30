def dollars_from_euros(euros):
    return (round(euros * 1.13, 2))

def dollars_from_euros_test():
    testing = True
    while testing:
        euro_amount = float(input("Enter the amount of euros: "))
        if euro_amount == -22:
            testing = False
        print("The dollar value for {euro_amount} ", dollars_from_euros(euro_amount))

def dollars_from_euros_automation_test():
    assert 113 == dollars_from_euros(100)
    assert 1.13 == dollars_from_euros(1)
    assert 0 == dollars_from_euros(0)
    assert -113 == dollars_from_euros(-100)
    assert (round(1.13 * 0.77, 2)) == dollars_from_euros(0.77)
    
    print("All automated tests passed!")


def automation_test_is_leap_year():
    print("Testing is_leap_year")

def manual_test_is_leap_year():
    testing = True
    while testing:
        year = int(input("Enter a year: "))
        if year == -22:
            testing = False
        

if __debug__:
    manual_test_is_leap_year() 
    automation_test_is_leap_year()

def main():
    dollars_from_euros_test()
    dollars_from_euros_automation_test()

if __name__ == "__main__":
    main()