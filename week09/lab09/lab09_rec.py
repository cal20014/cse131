def get_array():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(array)
    return array

def display_array(array):
    print(array)

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
    des = [0] * size
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

def main():
    array = get_array()
    display_array(array)
    sorted_array = sort_array(array)
    display_array(sorted_array)

if __name__ == "__main__":
    main()

