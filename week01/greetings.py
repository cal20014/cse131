



def get_name():
    name = input("what is your last name? ")
    return name
def get_gender():
    gender = input("What is your gender? (M/F) ")
    greeting = ''
    if gender.lower() == "m":
        greeting = "Mr."
    elif gender.lower() == "f":
        greeting = "Ms"
    else:
        print("that is not a valid gender")
    return gender

def display_message(gender, name):
    print(f"Hello, {gender} {name}")


def main():
    name = get_name()
    gender = get_gender()
    display_message(gender, name)

if __name__=="__main__":
    main()