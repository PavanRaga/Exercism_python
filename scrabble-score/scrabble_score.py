from string import ascii_lowercase


score1 = {
    1 : ['A','E','I','O','U','L','N','R','S','T'],
    2 : ['D', 'G'],
    3 : ['B','C','M','P'],
    4 : ['F','H','V','W','Y'],
    5 : ['K'],
    8 : ['J','X'],
    10 : ['Q','Z'],
}

def get_score(char):
    if char.isalpha():
        char = char.upper()
        score_char = int([x for x,y in score1.items() if y.count(char) == 1][0])
        return score_char
    else:
        return 0
   
def score(word):
    total_score = 0
    for alpha in list(word):
        total_score += get_score(alpha)
    return total_score