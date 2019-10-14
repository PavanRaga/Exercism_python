class Luhn(object):
    def __init__(self, card_num):
        self.card_num = list(card_num.replace(" ",""))

    def valid(self):
        card_num_len = len(self.card_num)
        if card_num_len <= 1 or not all(item.isdigit() for item in self.card_num):
            return False
        else:
            card_num_int = [int(digit) for digit in self.card_num]
            second_list = list(map(self.convert,card_num_int[-2::-2]))
            sum_code = sum(card_num_int[-1::-2],sum(second_list))
            if sum_code%10==0:
                return True
            return False

    @staticmethod
    def convert(digit):
        code = (digit) * (2)
        if code > 9:
            code -= 9
        return code

