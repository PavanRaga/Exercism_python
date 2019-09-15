from collections import Counter
import re

def count_words(sentence):
    return Counter(word.lower().strip("'") for word in re.findall(r"[a-zA-Z0-9']+", sentence))