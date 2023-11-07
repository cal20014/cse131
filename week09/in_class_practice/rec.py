def sum_power(num, power):
    if power == 0:
        return 1
    else:
        total = (num ** power) + sum_power(num, power - 1)
        # print(total)
        return total
    

def sum_pow_2(num):
    if num == 0:
        return 1
    power = 2 ** (num - 1)
    return power + sum_pow_2(num - 1)

def main():
    print(sum_power(2, 4))
    print(sum_pow_2(4))

if __name__ == "__main__":
    main()