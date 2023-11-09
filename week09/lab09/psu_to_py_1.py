def find_sorted_subarray(array, start_index):
    current_index = start_index

    while current_index < (len(array) - 1) and array[current_index] <= array[current_index + 1]:
        current_index += 1
    return current_index

def merge_sorted_subarrays(sourceArray, start_index, end_of_subarray01, end_of_subarray02, destinationArray):
    current_index_in_sub01 = start_index
    current_index_in_sub02 = end_of_subarray01
    destination_index = start_index

    while current_index_in_sub01 < end_of_subarray01 and current_index_in_sub02 < end_of_subarray02:
        if sourceArray[current_index_in_sub01] <= sourceArray[current_index_in_sub02]:
            destinationArray[destination_index] = sourceArray[current_index_in_sub01]
            current_index_in_sub01 += 1

        else:
            destinationArray[destination_index] = sourceArray[current_index_in_sub02]
            current_index_in_sub02 += 1
        # Increment destination index to iterate through the destination array   
        destination_index += 1

    while current_index_in_sub01 < end_of_subarray01:
        destinationArray[destination_index] = sourceArray[current_index_in_sub02]
        current_index_in_sub01 += 1
        destination_index += 1

    while current_index_in_sub02 < end_of_subarray02:
        destinationArray[destination_index] = sourceArray[current_index_in_sub02]
        current_index_in_sub02 += 1
        destination_index += 1

    

def sublist_sort(array):
    temp_array = array.copy()
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
            array, temp_array = temp_array, array

        return array


def run_test_cases():
    pass


def main():
    print("Hello, World!")

