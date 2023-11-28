def sort_rec(array, i_start, i_end):
    i_up = i_start
    i_down = i_end
    i_pivot = (i_start + i_end) // 2

    # End condition
    if i_up >= i_down or array == []:
        return array
    
    while i_up < i_down:

        while array[i_up] <= array[i_pivot] and i_up < i_pivot:
            i_up += 1

        while array[i_down] >= array[i_pivot] and i_down > i_pivot:
            i_down -= 1
        
        if i_pivot == i_up:
            i_pivot = i_down
        elif i_pivot == i_down:
            i_pivot = i_up
        
        # Swap
        array[i_up], array[i_down] = array[i_down], array[i_up]
        
    sort_rec(array, i_start, i_pivot - 1)
    sort_rec(array, i_pivot + 1, i_end)
    return array



def main():
    """
    The main function.
    """
    array = [31, 72, 10, 32, 18, 95, 25, 50]
    print(array)
    print(len(array))
    sorted_array = sort_rec(array, 0, len(array) - 1)
    print(sorted_array)


if __name__ == "__main__":
    main()