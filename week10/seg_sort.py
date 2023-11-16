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
    array = [31, 72, 10, 32, 18, 95, 25, 50]
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
    print(f"{yellow}====================================================") # Start yellow color
    print(f"{name}:")
    print(f"\t> {array}")
    print(f"===================================================={reset}")  # End yellow color

def sort_array(array, i_start, i_end):
    i_up = i_start
    i_down = i_end
    i_pivot = i_start + i_end // 2
    print(f"i_start: {i_start}, i_end: {i_end}, i_pivot: {i_pivot}")

    if i_start == i_end or array == []: # End Condition
        return array 
    
    outer_count = 0

    while i_up < i_down:
        print(f"count: {outer_count}")
        outer_count += 1
        inner_count = 0
        while array[i_up] <= array[i_pivot] and i_up < i_pivot:
            inner_count += 1
            print(f"inner_count: {inner_count}")
            print(f"array[i_up]: {array[i_up]}")
            i_up += 1
            print(f"array[i_up]: {array[i_up]}")
            print(f"i_up: {i_up}")

        while array[i_down] >= array[i_pivot] and i_down > i_pivot:
            print(f"inner_count: {inner_count}")
            inner_count += 1
            print(f"array[i_down]: {array[i_down]}")
            i_down -= 1
            print(f"array[i_down]: {array[i_down]}")
            print(f"i_down: {i_down}")

        print(f"inner_count_total: {inner_count}")
        inner_count += 1
        # Swap
        print(array[i_up], array[i_down])
        array[i_up], array[i_down] = array[i_down], array[i_up]
        array[i_up], array[i_down]

    sort_array(array, i_start, i_pivot)


    return array


def main():
    """
    The main function.
    """
    array = get_array()
    display_array(array, "Original array")
    sorted_array = sort_array(array, 0, len(array) - 1)
    display_array(sorted_array, "Sorted array")

if __name__ == "__main__":
    main()