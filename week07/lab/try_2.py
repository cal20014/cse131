def get_list():
    """
    Prompt user for a list of numbers, letters, or words, separated by commas.
    Returns a list of elements entered by the user.
    """
    user_input = input("Enter a list of numbers, letters, or words separated by commas: ")
    elements = user_input.split(',')
    # Attempt to convert numeric inputs to integers
    for i, element in enumerate(elements):
        try:
            elements[i] = int(element.strip())  # strip() to remove any leading/trailing spaces
        except ValueError:
            elements[i] = element.strip()  # If not a number, strip and keep the original string
    return elements


def display_list(list):
    """
    Display a list.
    """
   
    print(list)


def sublist_sort(array):
    temp_array = [0] * len(array)
    array_size = len(array)

    while True:
        is_sorted = True
        source_index = 0

        while source_index < array_size:
            end_first = find_next_sorted_subarray(array, source_index)
            end_second = find_next_sorted_subarray(array, end_first)

            # To ensure we don't go beyond the array's end
            end_second = min(end_second, array_size)

            merge_sorted_subarrays(array, source_index, end_first, end_second, temp_array)

            if end_second != array_size:
                is_sorted = False

            source_index = end_second

        array, temp_array = temp_array, array  # Swap the roles of the arrays for the next pass

        if is_sorted:
            break

    return array


def find_next_sorted_subarray(array, start_index):
    current_index = start_index

    while current_index < len(array) - 1 and array[current_index] <= array[current_index + 1]:
        current_index += 1

    return current_index + 1


def merge_sorted_subarrays(array, start_first, end_first, end_second, destination):
    index_first, index_second, destination_index = start_first, end_first, start_first

    while index_first < end_first and index_second < end_second:
        if array[index_first] <= array[index_second]:
            destination[destination_index] = array[index_first]
            index_first += 1
        else:
            destination[destination_index] = array[index_second]
            index_second += 1
        destination_index += 1

    while index_first < end_first:
        destination[destination_index] = array[index_first]
        index_first += 1
        destination_index += 1

    while index_second < end_second:
        destination[destination_index] = array[index_second]
        index_second += 1
        destination_index += 1


# Main function for testing
def main():
    test_array = [31, 72, 32, 10, 95, 50, 25, 18]
    sorted_array = sublist_sort(test_array)
    display_list(test_array)
    display_list(sorted_array)
    user_list = get_list()
    sorted_list = sublist_sort(user_list)
    display_list(user_list)
    display_list(sorted_list)

if __name__ == "__main__":
    main()
