def find_even_index(arr):   # find the point where there is an equal sum to the left and to the right
    for i in range(len(arr)):   # i will be the index of our value where this is true
        if sum(arr[:i]) == sum(arr[i+1:]):  # excluding i, check the sum to the left (lower index) and right (higher index)
            return i    # if they are equal return this index
    return -1   # if after looping through the list trying all indexes, no value meets like 3's condition, return -1


print(find_even_index([20, 10, 30, 10, 10, 15, 35]))

# done on codewars
