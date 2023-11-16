# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program sorts a list of numbers or strings using the sublist sort algorithm.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was transferring it from pseudocode to python code.
#      It was hard coding it out with out making mistakes and causing bugs.
#      The psuedocode was very helpful in making the coding process easier.
#      I also had a hard time with the test cases. I had a few errors
#      tha I had caused and had to fix. It took a bit to think it through.
#      Another hard part was figuring out how to color the text in the terminal.
#      This wasn't needed but I found it really fun.
# 5. How long did it take for you to complete the assignment?
#      It took me about 6 hours to complete the assignment.

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
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(array)
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

def merge_sorted_subarrays(source, destination, begin_sub01, begin_sub02, end_sub02):
    """
    Merges two sorted subarrays from 'source' into a single sorted subarray in 'destination'.

    Args:
        source (list): The source array containing the sorted subarrays.
        destination (list): The array where the merged subarray will be stored.
        begin_sub01 (int): The starting index of the first subarray.
        begin_sub02 (int): The starting index of the second subarray.
        end_sub02 (int): The ending index of the second subarray.

    Returns:
        list: The destination array with the merged subarrays.
    """
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
    """
    Sorts an array of numbers or strings using the sublist sort algorithm.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """

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
    """
    Runs test cases to validate the sort_array function.
    Displays the result of each test case in colored text.
    """
    # Test cases: an array of arrays for input and expected output
    test_inputs = [
        [6, 12, 11],  # Trace example Unsorted
        ["witch", "pumpkin", "ghost", "vampire", "zombie"],  # Array of Strings Unsorted,
        [3, 2, 1, 5, 4],  # Normal Unsorted
        [1, 2, 3, 4, 5],  # Already Sorted
        [5, 4, 3, 2, 1],  # Reverse Sorted
        ["This will Cause an assertion error"],
        [1],  # Single Element
        [],  # Empty Array
        
    ]
    expected_outputs = [
        [6, 11, 12],
        ["ghost", "pumpkin", "vampire", "witch", "zombie"],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ["Intentional Error"],
        [1],
        [],
    ]
    
    print(f"{cyan}\nRunning test cases...\n{reset}")
    count = 0
    success = 0
    fail = 0
    # Loop through each test case using its index
    for index in range(len(test_inputs)):
        count += 1
        # Sort the input array using the sort_array function
        sorted_array = sort_array(test_inputs[index])
        # Assert that the sorted_array matches the expected output

        if sorted_array == expected_outputs[index]:
            success += 1
        else:
            fail += 1

        try:
            assert sorted_array == expected_outputs[index]
            # If the assert does not fail, display a success message in green
            print(f"{green}====================================================")  # Start green color
            print(f"Case {count}: Test passed!\n \t> Input:           {test_inputs[index]}\n \t> Expected Output: {expected_outputs[index]}\n \t> Actual Output:   {sorted_array}")
            print(f"====================================================\n{reset}")  # End green color

        except AssertionError:
            # If the assert fails, display a failure message in red
            print(f"{red}====================================================")  # Start red color
            print(f"Case {count}:\n \t > Test failed for input: {test_inputs[index]}\n\t > Expected Output:       {expected_outputs[index]}\n\t > Actual Output:         {sorted_array}")
            print(f"====================================================\n{reset}")  # End red color

    print(f"{cyan}\nResults:{reset}")
    print(f"\t{purple}> Test cases ran: {count} {reset}")
    print(f"\t{green}> Test Cases Passed: {success}{reset}")
    print(f"\t{red}> Test Cases Failed: {fail}{reset}")

def main():
    DEBUG = True # Set this equal to True to run test cases
    array = get_array()

    print(f"{cyan}\nRunning Initial Sort....\n{reset}")
    display_array(array, "Original Array")
    sorted_array = sort_array(array)
    display_array(sorted_array, "Sorted Array")

    if DEBUG:
        run_test_cases()

if __name__ == "__main__":
    main()
