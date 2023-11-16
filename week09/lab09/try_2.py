def get_array():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(array)
    return array

def display_array(array):
    print(array)

def merge_sorted_subarrays(source, destination, begin_sub01, begin_sub02, end_sub02):
    index = begin_sub01
    end_sub01 = begin_sub02

    # Merging two sorted subarrays
    while begin_sub01 < end_sub01 and begin_sub02 < end_sub02:
        if source[begin_sub01] < source[begin_sub02]:
            destination[index] = source[begin_sub01]
            begin_sub01 += 1
        else:
            destination[index] = source[begin_sub02]
            begin_sub02 += 1
        index += 1

    # Copy any remaining elements from the first subarray
    while begin_sub01 < end_sub01:
        destination[index] = source[begin_sub01]
        begin_sub01 += 1
        index += 1

    # Copy any remaining elements from the second subarray
    while begin_sub02 < end_sub02:
        destination[index] = source[begin_sub02]
        begin_sub02 += 1
        index += 1

    return destination

def sort_array(array):
    size = len(array)
    src = array
    destination = [None] * len(array)
    print(destination)

    # Initially, each element is considered a sorted subarray of size 1
    # width = 1

    while width < size:
        for i in range(0, size, 2 * width):
            # Calculating the indices for the subarrays to be merged
            begin_sub01 = i
            begin_sub02 = min(i + width, size)
            end_sub02 = min(i + 2 * width, size)

            # Merging the subarrays
            merge_sorted_subarrays(src, destination, begin_sub01, begin_sub02, end_sub02)

        # Swap src and destination pointers
        src, destination = destination, src

        # Doubling the width on each iteration
        width *= 2

    return src

def main():
    unsorted_array = get_array()
    display_array(unsorted_array)
    sorted_array = sort_array(unsorted_array)
    display_array(sorted_array)

if __name__ == "__main__":
    main()
