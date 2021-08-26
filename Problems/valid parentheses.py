def valid_parentheses(string):  # takes in a string of bracket characters
    t = 0
    for i in string:
        if i == '(':
            t -= 1      # thinking of left brackets as negative and right brackets as positive
        if i == ')':
            t += 1
            if t > 0:
                return False

    # you can have potentially infinite left brackets (negative t value) as we don't know how many right brackets are coming
    # however, if there are too many right brackets in a row (positive t value), no amount of left brackets will be syntactically correct
    # e.g. ()) or )(

    if t == 0:          # if the sum of left and right brackets equals 0, it is valid
        return True
    else:
        return False


print(valid_parentheses("(())((()())())"))

# done on codewars
