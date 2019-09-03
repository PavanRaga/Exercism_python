class c_factors():
    def __init__(self,*factorsof):
        self.factorsof = factorsof
        self.factors_list = []
    def factors(self, n):
        for number in self.factorsof:
            if n%number == 0:
                self.factors_list.append(number)

def convert(number):
    o_factors = c_factors(3,5,7)
    o_factors.factors(number)
    result = ''
    for factors in o_factors.factors_list:
        if factors == 3:
            result = 'Pling'
        if factors == 5:
            result += 'Plang'
        if factors == 7:
            result += 'Plong'
    if not len(o_factors.factors_list):
        result = str(number)
    return result