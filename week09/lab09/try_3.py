def get_array():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(array)
    return array

def display_array(array):
    print(array)

def merge_sorted_subarrays(source, destination, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1, end2):
        if (begin1 < end1) and (begin2 >= end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1

    return destination

def sort_array(array):
    size = len(array)
    src = array
    des = [0] * size
    num = 2

    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] < src[end1]:
                end1 += 1

            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2

            while end2 < size and src[end2 - 1] < src[end2]:
                end2 += 1

            num += 1
            merge_sorted_subarrays(src, des, begin1, begin2, end2)
            begin1 = end2

        src, des = des, src

    return src

def main():
    array = get_array()
    display_array(array)
    sorted_array = sort_array(array)
    display_array(sorted_array)

if __name__ == "__main__":
    main()

