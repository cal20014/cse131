def get_user_input():
    """
    Prompts the user to enter a number or letter.

    The function requests input from the user, allowing them to enter either a number,
    a letter, or the word 'quit' to stop input.

    - return: The user's input as a string.
    """
    user_input = input("Enter a number or letter: ")
    return user_input

def get_list():
    """
    Gathers a list of user inputs until the user types 'quit'.

    This function continuously prompts the user to input numbers or letters,
    appending them to a list. The input is converted to an integer if possible.
    If the user enters 'quit', the function stops asking for input and returns the list.

    - return: A list of user inputs, with numbers converted to integers and other inputs as strings.
    """
    user_list = []
    getting_input = True
    while getting_input:
        user_input = get_user_input()
        if user_input.lower() == "quit":
            getting_input = False
        else:
            try:
                converted_input = int(user_input)  # Try to convert to an integer
                user_list.append(converted_input)
            except ValueError:
                user_list.append(user_input)  # Append as a string if conversion fails
            print(user_list)
    return user_list


def display_list(any_list):
    """
    Prints the given list.

    - param any_list: A list that will be printed to the console.
    """
    print(any_list)

def find_sorted_subarray(array, start_index):
    """
    Finds the end index of a sorted subarray starting from a given index.

    The function searches for a contiguous increasing sequence in 'array'
    starting from 'start_index'. The search stops when it encounters an
    element that is greater than the next, or when it reaches the end of
    the array.

    - param array: The list in which to find the sorted subarray.
    - param start_index: The starting index from which to search for the sorted subarray.
    - return: The index just after the end of the sorted subarray.
    """
    current_index = start_index
    while current_index < len(array) - 1 and array[current_index] <= array[current_index + 1]:
        current_index += 1
    return current_index + 1


def merge_sorted_subarrays(sourceArray, start_index, end_of_subarray01, end_of_subarray02, destination):
    """
    Merges two adjacent sorted subarrays from 'sourceArray' into 'destination'.

    This function merges elements from two sorted subarrays (specified by their
    starting and ending indices) into a single sorted array. The result is stored
    in 'destination', starting at 'start_index'.

    - param sourceArray: The array containing the sorted subarrays to be merged.
    - param start_index: The starting index of the first sorted subarray.
    - param end_of_subarray01: The ending index of the first sorted subarray.
    - param end_of_subarray02: The ending index of the second sorted subarray.
    - param destination: The array where the merged sorted subarray will be stored.
    """
    current_index_in_sub01 = start_index
    current_index_in_sub02 = end_of_subarray01
    destination_index = start_index

    while current_index_in_sub01 < end_of_subarray01 and current_index_in_sub02 < end_of_subarray02:
        if sourceArray[current_index_in_sub01] <= sourceArray[current_index_in_sub02]:
            destination[destination_index] = sourceArray[current_index_in_sub01]
            current_index_in_sub01 += 1
        else:
            destination[destination_index] = sourceArray[current_index_in_sub02]
            current_index_in_sub02 += 1
        destination_index += 1

    while current_index_in_sub01 < end_of_subarray01:
        destination[destination_index] = sourceArray[current_index_in_sub01]
        current_index_in_sub01 += 1
        destination_index += 1

    while current_index_in_sub02 < end_of_subarray02:
        destination[destination_index] = sourceArray[current_index_in_sub02]
        current_index_in_sub02 += 1
        destination_index += 1

def sublist_sort(array):
    """
    Sorts the given list using a modified merge sort algorithm.

    This function sorts 'array' in place by iteratively merging sorted subarrays.
    A temporary array, 'temp_array', is used for merging. The sort is complete
    when a single pass through 'array' requires no further merging.

    - param array: The list to be sorted.
    - return: The sorted list.
    """
    temp_array = [0] * len(array)
    array_size = len(array)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        start_index = 0

        while start_index < array_size:
            end_of_subarray01 = find_sorted_subarray(array, start_index)
            end_of_subarray02 = find_sorted_subarray(array, end_of_subarray01)

            if end_of_subarray02 > array_size:
                end_of_subarray02 = array_size
                
            merge_sorted_subarrays(array, start_index, end_of_subarray01, end_of_subarray02, temp_array)

            if end_of_subarray02 != array_size:
                is_sorted = False

            start_index = end_of_subarray02

        array, temp_array = temp_array, array  # Swap the roles of the arrays for the next pass

    return array




def main():
    new_list = get_list()
    print(new_list)

    original_list = [8, 3, 1, 7, 0, 10, 2]
    sorted_list = sublist_sort(original_list)
    display_list(original_list)
    display_list(sorted_list)

if __name__ == '__main__':
    main()