def personal_best(scores):
    for i in scores:
        if isinstance(i, str):
            raise ValueError('Please enter only numbers')
    return max(scores)