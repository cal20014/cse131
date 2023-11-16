def get_user_input():
    user_input = input("Enter a number or letter: ")
    return user_input

def get_list():
    user_list = []
    getting_input = True
    while getting_input:
        user_input = get_user_input()
        if user_input.lower() == "quit":
            getting_input = False
        else:
            # Attempt to convert user input to an integer, if possible
            try:
                user_input = int(user_input)
            except ValueError:
                pass  # Keep the input as a string if it's not a number
            user_list.append(user_input)
            print(user_list)
    return user_list
    
def display_list(any_list):
    print(any_list)

def find_sorted_subarray(array, start_index):
    current_index = start_index

    while current_index < len(array) - 1 and array[current_index] <= array[current_index + 1]:
        current_index += 1 # increment current_index by 1

    return current_index + 1

def merge_sorted_subarrays(sourceArray, start_index, end_of_subarray01, end_of_subarray02, destination):
    # Initialize pointers for each subarray and the destination array
    current_index_in_sub01 = start_index        # Points to the current element in the first subarray
    current_index_in_sub02 = end_of_subarray01  # Points to the current element in the second subarray
    destination_index = start_index             # Points to the current position in the destination array

    # Iterate as long as there are elements in both subarrays
    while current_index_in_sub01 < end_of_subarray01 and current_index_in_sub02 < end_of_subarray02:
        
        # Compare current elements of the subarrays
        if sourceArray[current_index_in_sub01] <= sourceArray[current_index_in_sub02]:
            # If element in first subarray is smaller, copy it to the destination array
            destination[destination_index] = sourceArray[current_index_in_sub01]
            current_index_in_sub01 += 1  # Move to the next element in the first subarray
        else:
            # If element in second subarray is smaller, copy it to the destination array
            destination[destination_index] = sourceArray[current_index_in_sub02]
            current_index_in_sub02 += 1  # Move to the next element in the second subarray
        destination_index += 1  # Move to the next position in the destination array

    # If there are remaining elements in the first subarray, copy them to the destination array
    while current_index_in_sub01 < end_of_subarray01:
        destination[destination_index] = sourceArray[current_index_in_sub01]
        current_index_in_sub01 += 1
        destination_index += 1

    # If there are remaining elements in the second subarray, copy them to the destination array
    while current_index_in_sub02 < end_of_subarray02:
        destination[destination_index] = sourceArray[current_index_in_sub02]
        current_index_in_sub02 += 1
        destination_index += 1
    
def sublist_sort(array):
    sourceArray01 = array
    sourceArray02 = [None] * len(array)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        start_index = 0
        while start_index < len(array):
            end_of_subarray01 = find_sorted_subarray(array, start_index)
            end_of_subarray02 = find_sorted_subarray(array, end_of_subarray01)
            
            # To ensure we don't go beyond the array's end
            end_of_subarray02 = min(end_of_subarray02, len(array))
            
            merge_sorted_subarrays(array, start_index, end_of_subarray01, end_of_subarray02, sourceArray02)
            if end_of_subarray02 != len(array):
                is_sorted = False

            # Move the start index to the end of the merged subarray for the next iteration
            start_index = end_of_subarray02

        sourceArray01, sourceArray02 = sourceArray02, sourceArray01
        
        if is_sorted:
            is_sorted = True
    return array



def main():
    original_list = get_list()
    sorted_list = sublist_sort(original_list)
    display_list(original_list)
    display_list(sorted_list)

if __name__ == '__main__':
    main()