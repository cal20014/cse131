def get_array():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(array)
    return array

def display_array(array, name):
    print("==================================")
    print(f"{name}:")
    print(f"\t> {array}")
    print("==================================")

def merge_sorted_subarrays(source, destination, begin_sub01, begin_sub02, end_sub02):
    end_sub01 = begin_sub02

    for i in range(begin_sub01, end_sub02):
        if (begin_sub01 < end_sub01) and (begin_sub02 >= end_sub02 or source[begin_sub01] < source[begin_sub02]):
            destination[i] = source[begin_sub01]
            begin_sub01 += 1
        else:
            destination[i] = source[begin_sub02]
            begin_sub02 += 1

    return destination

def sort_array(array):
    size = len(array)
    src = array
    des = [None] * size
    num = 2

    while num > 1:
        num = 0
        begin_sub01 = 0

        while begin_sub01 < size:
            end_sub01 = begin_sub01 + 1
            while end_sub01 < size and src[end_sub01 - 1] < src[end_sub01]:
                end_sub01 += 1

            begin_sub02 = end_sub01
            if begin_sub02 < size:
                end_sub02 = begin_sub02 + 1
            else:
                end_sub02 = begin_sub02

            while end_sub02 < size and src[end_sub02 - 1] < src[end_sub02]:
                end_sub02 += 1

            num += 1
            merge_sorted_subarrays(src, des, begin_sub01, begin_sub02, end_sub02)
            begin_sub01 = end_sub02

        src, des = des, src

    return src


def run_test_cases():
    # Test cases: an array of arrays for input and expected output
    test_inputs = [
        [6, 12, 11],  # Trace example Unsorted
        ["witch", "pumpkin", "ghost", "vampire", "zombie"],  # Array of Strings Unsorted,
        [3, 2, 1, 5, 4],  # Normal Unsorted
        [1, 2, 3, 4, 5],  # Already Sorted
        [5, 4, 3, 2, 1],  # Reverse Sorted
        [1],  # Single Element
        [],  # Empty Array
        
    ]
    expected_outputs = [
        [6, 11, 12],
        ["ghost", "pumpkin", "vampire", "witch", "zombie"],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1],
        [],
    ]
    
    print("\nRunning test cases...\n")
    count = 0
    # Loop through each test case using its index
    for index in range(len(test_inputs)):
        count += 1
        # Sort the input array using the sort_array function
        sorted_array = sort_array(test_inputs[index])
        # Assert that the sorted_array matches the expected output
        assert sorted_array == expected_outputs[index], f"Case {count}: Test failed for input: {test_inputs[index]} Expected Output: {expected_outputs[index]} Actual Output: {sorted_array}"
        # If the assert does not fail, display a success message
        print("==================================")
        print(f"Case {count}: Test passed!\n \t> Input:           {test_inputs[index]}\n \t> Expected Output: {expected_outputs[index]}\n \t> Actual Output:   {sorted_array}")
        print("==================================\n")

    print(f"Ran {count} test cases.")
    print(f"All test {count} cases passed!\n")

def main():
    DEBUG = True # Set this equal to True to run test cases
    array = get_array()
    display_array(array, "Original Array")
    sorted_array = sort_array(array)
    display_array(sorted_array, "Sorted Array")

    if DEBUG:
        run_test_cases()

if __name__ == "__main__":
    main()

