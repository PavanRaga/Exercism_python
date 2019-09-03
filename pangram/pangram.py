import string

def is_pangram(sentence):
    alpha = list(string.ascii_lowercase)
    if sentence:
        s_list = list(sentence.lower())
        for char in s_list:
            try:
                alpha.remove(char)
            except ValueError:
                pass
        if len(alpha) == 0:
            return True
        else:
            return False
    else:
        return False