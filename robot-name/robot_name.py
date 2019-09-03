from random import choice,randint
import random
import string

class Robot(object):
    @staticmethod
    def random_char(num):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(num))
    
    @staticmethod
    def random_int():
        return str(randint(100,999))

    def __init__(self):
        self.name = Robot.random_char(2) + Robot.random_int()

    def reset(self):
        name = self.name
        self.__init__()
        if name == self.name:
            self.__init__()