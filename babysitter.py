class Babysitter():
    def __init__(self, start_time, end_time, family):
        self.start_time = start_time
        self.end_time = end_time
        self.family = family
        self.has_babysat_tonight = False
        self.times = ["5p", "6p", "7p", "8p", "9p", "10p", "11p", "12a", "1a", "2a", "3a", "4a"]

    def is_valid_start_time(self):
        if self.start_time in self.times:
            return True
        return False

    def is_valid_end_time(self):
        if self.end_time in self.times:
            return True
        return False

    def has_not_babysat_tonight(self):
        return self.has_babysat_tonight
