def weight(s):          # need to sort a list of weight integers by the sum of their digits
    weight_value = 0
    for i in s:
        weight_value += int(i)
    return weight_value         # creating a function which calculates this


def order_weight(string):
    weight_list = string.split()    # splitting the string so we can sort the weights
    ordered = sorted(weight_list, key=lambda x: (weight(x), x))     # sorting with 2 criteria:
    return ' '.join(ordered)
# sorting with 2 criteria; the weight function and the position of the value in the original list but sorted (x)


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))

# done on codewars
