import re

def abbreviate(words):
    wordss = re.split(r'[^\w\']|_',words)
    return "".join([word[0].upper() for word in wordss if word != ""])