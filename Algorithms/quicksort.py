def quicksort(array):   # understanding recursion
    left = []
    right = []
    if len(array) <= 1:  # base case. this must be set or it will recurse forever
        return array    # if the array only has 1 number, there's nothing to sort
    else:
        pivot = array.pop()  # set last number as pivot. pivot won't be sorted as it is our reference point
        for i in array:
            if i > pivot:
                right.append(i)     # group bigger numbers to the right, smaller to the left
            elif i <= pivot:
                left.append(i)
        return quicksort(left) + [pivot] + quicksort(right)
        # sorts the left and right until it reaches the base case, maintaining the pivot each recursion


print(quicksort([17, 9, 18, 10, 4, 6, 1, 19, 12, 15, 16, 2, 7, 13, 5]))
