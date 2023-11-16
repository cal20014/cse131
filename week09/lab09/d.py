def combine(source, destination, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1, end2):
        if (begin1 < end1) and (begin2 >= end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1

    return destination

def sort(array):
    size = len(array)
    src = array.copy()
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
            combine(src, des, begin1, begin2, end2)
            begin1 = end2

        src, des = des, src

    return src

# Example usage
example_array = [34, 7, 23, 32, 5, 62]
sorted_array = sort(example_array)
print(sorted_array)
sorted_array

