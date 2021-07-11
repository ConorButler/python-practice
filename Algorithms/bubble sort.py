def bubble_sort(array):
    ordered = False

    while ordered == False:     # everything below (lines 5-9) will be run before this is checked again
        ordered = True      # assume it's ordered until proven otherwise
        for i in range(len(array)-1):
            if array[i] > array[i+1]:   # if value to the right is smaller, it's unordered
                    ordered = False
                    array[i], array[i+1] = array[i+1], array[i]     # swap these values
    return array


print(bubble_sort([1, 18, 2, 9, 20, 13, 11, 19, 12, 16, 7, 10, 17]))
