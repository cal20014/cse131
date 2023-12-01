data_set = list(range(-50, 50, 1))
print(data_set)
print()


def is_even(x):
    return not x % 2

even_nums = list(filter(is_even, data_set))
print(even_nums)

even_nums = list(filter(lambda x : not x % 2, data_set))
print(even_nums)

# even_nums = list(filter(is_even, data_set))
# print(even_nums)

def convert_to_money(x):
    return f"${x:.2f}"

money_list = list(map(convert_to_money, data_set))
print(money_list)



new_data_set = list(range(1, 100))
import functools

def add_reduce(x, y):
    print(f"Adding {x} and {y}")
    return x + y

total = functools.reduce(add_reduce, data_set)

total = functools.reduce(lambda x, y : x + y, data_set)

print(f"The total is: {total}")
total = functools.reduce(lambda x, y : x + y, new_data_set)

print(f"The total is: {total}")