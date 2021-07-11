def binary_search(array, element):   # return the index of the element
    left = 0
    right = len(array)
    while left < right:     # this should always be true so it makes the if statements loop
        mid = (left + right) // 2
        if array[mid] == element:   # if mid = element we are looking for just return mid
            return mid
        elif array[mid] < element:    # if less than element, ignore the left, search the right
            left = mid
        elif array[mid] > element:  # vice versa
            right = mid
    return left


print(binary_search([2, 5, 7, 8, 12, 14, 16, 18, 21, 23, 28, 33], 7))

# the array we input must be sorted
