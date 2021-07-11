def lucky_numbers(l,h):
    numstring = [str(i) for i in range(l, h+1)]  # creating a list of numbers between l and h in string form
    count = 0                                    # counter
    for j in numstring:
        if '6' in j and '8' not in j:
            count += 1
        if '8' in j and '6' not in j:
            count += 1
    return count

print(lucky_numbers(1,100))


