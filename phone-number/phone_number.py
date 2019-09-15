import re

class Phone(object):
    def __init__(self, phone_number):
        self.digits = re.findall(r'(\d\d[\d]+)', phone_number)
        self.number = ''.join(self.digits)
        self.area_code =  ''.join(self.digits)
    def pretty(self):
        return '({0}) {1}-{2}'.format(self.digits.group(1),self.digits.group(2),self.digits.group(3),)
        #self.phone_number = phone_number

print(Phone("(223) 456-7890").number)