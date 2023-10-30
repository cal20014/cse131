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

    # If there are remaining elements in the first subarray, copy them
    while current_index_in_sub01 < end_of_subarray01:
        destination[destination_index] = sourceArray[current_index_in_sub01]
        current_index_in_sub01 += 1
        destination_index += 1

    # If there are remaining elements in the second subarray, copy them
    while current_index_in_sub02 < end_of_subarray02:
        destination[destination_index] = sourceArray[current_index_in_sub02]
        current_index_in_sub02 += 1
        destination_index += 1
