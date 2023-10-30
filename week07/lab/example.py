def get_user_input():
    """
    Prompt user for a single number or letter. Returns the input as a string.
    """
    user_input = input("Enter a number, letter, or 'quit' to stop: ")
    return user_input

def get_list():
    """
    Continuously prompts the user for input until 'quit' is entered.
    Converts numeric inputs to integers. Returns a list of elements entered by the user.
    """
    user_list = []
    getting_input = True

    while getting_input:
        input_value = get_user_input()
        if input_value.lower() == "quit":
            getting_input = False
        else:
            # Attempt to convert user input to an integer, if possible
            try:
                input_value = int(input_value)
            except ValueError:
                pass  # Keep the input as a string if it's not a number
            user_list.append(input_value)
            print("Current list:", user_list)

    return user_list

def display_list(any_list):
    """
    Display a list.
    """
    print("List:", any_list)

def find_sorted_subarray(source_array, start_index):
    """
    Finds the end index of a sorted subarray starting from a given index.
    """
    current_index = start_index
    while current_index < len(source_array) - 1 and source_array[current_index] <= source_array[current_index + 1]:
        current_index += 1
    return current_index + 1

def merge_sorted_subarrays(source_array, start_index, mid_index, end_index, merged_array):
    """
    Merges two sorted subarrays into a single sorted array.
    """
    index1, index2, merge_index = start_index, mid_index, start_index

    while index1 < mid_index and index2 < end_index:
        if source_array[index1] <= source_array[index2]:
            merged_array[merge_index] = source_array[index1]
            index1 += 1
        else:
            merged_array[merge_index] = source_array[index2]
            index2 += 1
        merge_index += 1

    while index1 < mid_index:
        merged_array[merge_index] = source_array[index1]
        index1 += 1
        merge_index += 1

    while index2 < end_index:
        merged_array[merge_index] = source_array[index2]
        index2 += 1
        merge_index += 1

def sublist_sort(main_array):
    """
    Sorts the main array using the natural merge sort algorithm.
    """
    temp_array = [0] * len(main_array)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        start_index = 0

        while start_index < len(main_array):
            mid_index = find_sorted_subarray(main_array, start_index)
            end_index = find_sorted_subarray(main_array, mid_index)
            
            end_index = min(end_index, len(main_array))

            merge_sorted_subarrays(main_array, start_index, mid_index, end_index, temp_array)

            if end_index != len(main_array):
                is_sorted = False
            start_index = end_index

        main_array, temp_array = temp_array, main_array

    return main_array

def main():
    original_list = get_list()
    sorted_list = sublist_sort(original_list)
    display_list(original_list)
    display_list(sorted_list)

if __name__ == '__main__':
    main()
