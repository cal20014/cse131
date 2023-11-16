def get_array():
    
    return [9, 8, 7, 6, 5, 4, 3, 2, 1]

def display_array(array):
    print(array)

def merge_sorted_subarrays(source, destination, begin_sub01, begin_sub02, end_sub02):
    end_sub01 = begin_sub01

    for index in range(begin_sub01, end_sub02):
        if (begin_sub01 < end_sub01) and (begin_sub02 == end_sub02 or source[begin_sub01] < source[begin_sub02]):
            destination[index] = source[begin_sub01]
            begin_sub01 += 1
        else:
            destination[index] = source[begin_sub02]
            begin_sub02 += 1

    return destination

def sort_array(array):
    size = len(array)
    src = array
    destination = array.copy()
    num = 2

    while num > 1:
        num = 0
        begin_sub01 = 0

        while begin_sub01 < size:
            end_sub01 = begin_sub01 + 1
            while end_sub01 < size and src[end_sub01 - 1] <= src[end_sub01]:
                end_sub01 += 1

            begin_sub02 = end_sub01
            if begin_sub02 < size:
                end_sub02 = begin_sub02 + 1
            else:
                end_sub02 = begin_sub02

            while end_sub02 < size and src[end_sub02 - 1] <= src[end_sub02]:
                end_sub02 += 1

            num += 1

            merge_sorted_subarrays(src, destination, begin_sub01, end_sub01, end_sub02)
            begin_sub01 = end_sub02
        # swap src and destination pointers
        src, destination = destination, src

    return src

def main():
    array = get_array()
    sorted_array = sort_array(array)
    display_array(array)
    display_array(sorted_array)

if __name__ == "__main__":
    main()