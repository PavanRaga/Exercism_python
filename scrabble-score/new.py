score1 = {
    1 : ['A','E','I','O','U','L','N','R','S','T'],
    2 : ['D', 'G'],
    3 : ['B','C','M','P'],
    4 : ['F','H','V','W','Y'],
    5 : ['K'],
    8 : ['J','X'],
    10 : ['Q','Z'],
}

print(score1[1])

if 'P' in score1[3]:
    print(1)
else:
    print(0)
#for i in score1.keys():
