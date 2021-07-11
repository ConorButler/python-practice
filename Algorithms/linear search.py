def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return 'Element index: ', i
    return 'Element not found'


print(linear_search([20, 9, 2, 13, 19, 5, 12, 14, 10, 8, 1, 3, 11, 18, 6], 8))

print(linear_search([20, 9, 2, 13, 19, 5, 12, 14, 10, 8, 1, 3, 11, 18, 6], 30))
