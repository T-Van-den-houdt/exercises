class Duration:
    def __init__(self, time_in_seconds):
        self.time = time_in_seconds

    @staticmethod
    def from_seconds(seconds):
        return Duration(time_in_seconds=seconds)

    @property
    def seconds(self):
        return self.time

    @staticmethod
    def from_minutes(minutes):
        return Duration(time_in_seconds=minutes * 60)

    @property
    def minutes(self):
        return self.time / 60

    @staticmethod
    def from_hours(hours):
        return Duration(time_in_seconds=hours * 3600)

    @property
    def hours(self):
        return self.time / 3600