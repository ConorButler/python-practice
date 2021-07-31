def latest(scores):
    for i in scores:
        if isinstance(i, str):
            raise ValueError('Please enter only numbers')
    return scores[-1]
