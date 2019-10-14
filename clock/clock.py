class Clock(object):
    def __init__(self, hour, minute):
        temp = 0
        if hour < 0:
            temp = 12
        self.hour = str(hour%12 + temp)
        if len(self.hour) == 1:
            self.hour = "0" + self.hour
        self.minute = str(minute%60)
        if len(self.minute) == 1:
            self.minute = "0" + self.minute

    def __repr__(self):
        return self.hour + ":" + self.minute

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            return True
        return False

    def __add__(self, minutes):
        self.minute += minutes
        while self.minute > 60:
            self.hour += 1
            self.minute -= 60

    def __sub__(self, minutes):
        self.minute -= minutes
        while self.minute < 60:
            self.hour -= 1
            self.minute += 60

#print(Clock(-,0))