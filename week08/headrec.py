def add(value1, value2):
    if value2 == 0:
        print(value1, value2)
        return value1
    else:
        print(value1, value2)
        return 1 + add(value1, value2 - 1)
    
def add(value1, value2):
    if value2 == 0:
        print(value1, value2)
        return value1
    else:
        print(value1, value2)
        sum = 1 + add(value1, value2 - 1)
        print("sum", sum)
        return sum
    

def add_again(value1, value2):
    if value2 == 0:
        print(value1, value2)
        return value1
    else:
        print(value1, value2)
        sum = add_again(value1 + 1, value2 - 1)
        print("sum", sum)
        return sum
    

def main():
    print(add(5, 3))
    print(add_again(5, 3))
    print(add(10, 5))
    print(add_again(10, 5))

if __name__ == "__main__":
    main()