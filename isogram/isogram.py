from collections import Counter

def is_isogram(string):
    string = string.lower()
    counter_dict = Counter(list(string))

    if len([value for key,value in counter_dict.items() if value > 1 and key.isalpha()]):
        return False
    return True