def fibonacci(n):
    seq = []    # initialise an array to store the fibonacci numbers
    if n <= 0:
        return seq
    elif n == 1:        # complying with the rules of fibonacci
        return [0]
    seq = [0, 1]
    while len(seq) < n:     # until we do the following n times:
        seq.append(sum(seq[-2:]))   # sum the previous 2 numbers and add this to the end of the sequence
    return seq


print(fibonacci(10))

# done on codewars
