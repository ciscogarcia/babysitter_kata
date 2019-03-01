class Babysitter():
    def __init__(self, start_time, end_time, family):
        self.start_time = start_time
        self.end_time = end_time
        self.family = family
        self.has_babysat_tonight = False
        self.times = ["5:00pm", "6:00pm", "7:00pm", "8:00pm", "9:00pm", "10:00pm", "11:00pm", "12:00am", "1:00am", "2:00am", "3:00am", "4:00am"]

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
