

def get_birth_year():
    b_year = int(input("What year were you born? "))
    return b_year

def calc_age(b_year):
    current_year = 2023
    age = current_year - b_year
    return age


def main():
    b_year = get_birth_year()
    age = calc_age(b_year)
    print(f"You will turn {age} this year")

if __name__=="__main__":
    main()