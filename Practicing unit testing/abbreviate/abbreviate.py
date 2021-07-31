def abbreviate(text):
    if not text[0].isalpha():
        raise ValueError('Please start with a letter.')
    a = text[0]
    for i in range(len(text)-1):  # to stop error if sentence ends in punctuation
        if not text[i].isalpha():  # if char is not in the alphabet
            if text[i+1].isalpha():  # append the next char if it is in the alphabet
                a += text[i+1]
    return a.upper()


print(abbreviate('1First In, First Out'))
