def get_user_input():
    user_input = input("Enter a number or letter: ")
    return user_input

def get_list():
    user_list = []
    getting_input = True
    while getting_input:
        question = input("Do you want to add to the list? (y/n): ")
        if question.lower() == "y":
            user_input = get_user_input()
            user_list.append(user_input)
            print(user_list)
        elif question.lower() == "n":
            getting_input = False
        else:
            print("Invalid input: Please enter y or n")
    
def display_list(any_list):
    print(any_list)

def find_sorted_subarray(array, start_index):
    current_index = start_index

    while current_index < len(array) - 1 and array[current_index] <= array[current_index + 1]:
        current_index += 1 # increment current_index by 1

    return current_index + 1

def merge_sorted_subarrays(sourceArray, start_index, end_of_subarray01, end_of_subarray02, destination):
    current_index_in_sub01 = start_index
    current_index_in_sub02 = end_of_subarray01
    destination_index = start_index

    while current_index_in_sub01 < end_of_subarray01 and current_index_in_sub02 < end_of_subarray02:
        if sourceArray[current_index_in_sub01] <= sourceArray[end_of_subarray02]:
            start_index += 1
        else:
            destination[start_index] = sourceArray


    

def sublist_sort(array):
    sourceArray01 = array
    sourceArray02 = [0] * len(array)
    start_index = 0
    is_sorted = False
    while is_sorted:
        while start_index < len(array):
            end_of_subarray01 = find_sorted_subarray(array, start_index)
            end_of_subarray02 = find_sorted_subarray(array, end_of_subarray01)
            merge_sorted_subarrays(array, start_index, end_of_subarray01, end_of_subarray02, sourceArray02)

            if end_of_subarray02 == len(array):
                is_sorted = True

            start_index = end_of_subarray02

        sourceArray01, sourceArray02 = sourceArray02, sourceArray01
        
    return array



def main():
    pass

if __name__ == '__main__':
    main()