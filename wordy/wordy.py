
WORD = ('plus', 'minus', 'multiplied by', 'divided by')
SIGN = ('+', '-', '*', '/')
ERROR = ValueError('Invalid question format')

stack = []

import re

def answer(question):

    filter_question = question[7:-1]

    for i in range(4):
        filter_question = re.sub(WORD[i],SIGN[i],filter_question)
    try:
        eval(filter_question)
    except (SyntaxError):
        raise ERROR

    # if more than one operator paired, i.e. + +
    if re.search(r'-?\d+ (\D){2,} -?\d+', filter_question):
        raise ERROR
    # add parenthesis for evaluating from left to right
    equation = re.sub(r'(-?\d+ \D -?\d+)', r'(\1)', filter_question)

    return eval(equation)
