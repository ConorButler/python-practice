def digital_root(n):    # find the sum of the digits, repeating until a single digit number is produced
    n = str(n)  # convert the input (a non negative integer) into a string so we can iterate over it
    while len(n) > 1:   # until n becomes a single digit
        y = 0   # y stores our sum
        for i in n:
            y += int(i)     # iterating through the number string (n), so must convert back to int
        n = str(y)      # make this sum a string again so we can check the length and iterative over it again if need be
    return int(n)   # convert back to int when while loop finishes


print(digital_root(132189))

# done on codewars
