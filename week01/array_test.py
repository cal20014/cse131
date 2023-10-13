def calc_sum_elements(num_array):
    """
    Sum numbers in an array
    """
    total = 0
    for num in num_array:
        total += num
    return total


def main():
    num_array = [1, 2, 3, 4, 5]
    total = calc_sum_elements(num_array)
    print(f"Total: {total}")

