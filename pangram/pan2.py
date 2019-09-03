from collections import Counter

def is_pangram(sentence):
    print(Counter(filter(lambda x: x.isalpha(), sentence.lower())))

is_pangram("a"*26)