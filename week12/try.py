import matplotlib.pyplot as plt
import numpy as np
import random



red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
purple = "\033[35m"
cyan = "\033[96m"
reset = "\033[0m"


def get_array():
    """
    Generates and return a predefined array of integers.
    
    Returns:
        list: A list of integers.
    """
    # array = [31, 72, 10, 32, 18, 95, 25, 50]
    array = [5, 3, 8, 4, 2, 7, 1, 10, 6, 9]
    # array = [2, 1]
    print(array)
    return array

def display_array(array, name):
    """
    Displays an array with a given name in a formatted style with colored text.

    Args:
        array (list): The array to display.
        name (str): A descriptive name for the array.
    """
    print(f"====================================================")
    print(f"{name}:")
    print(f"\t> {array}")
    print(f"====================================================")


def sort_rec(array, i_start, i_end, counter):
    i_up = i_start
    i_down = i_end
    i_pivot = (i_start + i_end) // 2

    # End condition
    if i_up >= i_down or not array:
        return array, counter
    
    while i_up < i_down:
        counter += 1
        while array[i_up] <= array[i_pivot] and i_up < i_pivot:
            i_up += 1
            counter += 1

        while array[i_down] >= array[i_pivot] and i_down > i_pivot:
            i_down -= 1
            counter += 1
        
        if i_pivot == i_up:
            i_pivot = i_down
        elif i_pivot == i_down:
            i_pivot = i_up

        array[i_up], array[i_down] = array[i_down], array[i_up]

    array, counter = sort_rec(array, i_start, i_pivot - 1, counter)
    array, counter = sort_rec(array, i_pivot + 1, i_end, counter)
    return array, counter


def main():
    input_sizes = [0, 10, 100, 1000, 10000, 100000, 1000000]
    counters = []

    for n in input_sizes:
        array = random.sample(range(n), n)
        _, counter = sort_rec(array, 0, len(array) - 1, 0)
        counters.append(counter)

    plt.plot(input_sizes, counters)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input size (n)')
    plt.ylabel('Number of operations')
    plt.show()

if __name__ == "__main__":
    main()
   