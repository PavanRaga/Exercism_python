get_last_one = slice(-1,-2,-1)
get_last_three = slice(-1,-4,-1)

def latest(scores):
    if scores:
        return scores[get_last_one][0]
    else:
        pass

def personal_best(scores):
    if scores:
        scores.sort()
        return scores[get_last_one][0]
    else:
        pass

def personal_top_three(scores):
    if scores:
        scores.sort()
        return scores[get_last_three]
    else:
        pass
