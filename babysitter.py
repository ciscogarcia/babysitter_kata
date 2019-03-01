class Babysitter():
    def __init__(self, start_time, end_time, family):
        self.start_time = start_time
        self.end_time = end_time
        self.family = family
        self.times = [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]

    def is_valid_start_time(self):
        if self.start_time in self.times:
            return True
        return False

