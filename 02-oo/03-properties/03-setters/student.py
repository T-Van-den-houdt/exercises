# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, new_hour):
        if 0 <= new_hour <= 23:
            self.__hours = new_hour
        else:
            raise ValueError

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, new_minute):
        if 0 <= new_minute <= 59:
            self.__minutes = new_minute
        else:
            raise ValueError

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, new_second):
        if 0 <= new_second <= 59:
            self.__seconds = new_second
        else:
            raise ValueError