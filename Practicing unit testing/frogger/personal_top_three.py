def personal_top_three(scores):
    for i in scores:
        if isinstance(i, str):
            raise ValueError('Please enter only numbers')
    return sorted(scores, reverse=True)[:3]
