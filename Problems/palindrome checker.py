def palindrome(s):
    x = 0
    y = len(s)-1
    while x < y:    # move to the middle from opposite ends of the string
        if s[x] != s[y]:
            return False    # if one character is not equal to it's opposite index, return False
        x += 1
        y -= 1
    return True     # if it made it through without any differences, it's a palindrome

print(palindrome('kaaaaaayaaaaaak'))