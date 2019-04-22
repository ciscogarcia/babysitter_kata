class Babysitter():
    def __init__(self, start_time, end_time, family):
        self.start_time = start_time
        self.end_time = end_time
        self.family = family
        self.babysat_tonight = False
        self.times = ["5:00pm", "6:00pm", "7:00pm", "8:00pm", "9:00pm", "10:00pm", "11:00pm", "12:00am", "1:00am", "2:00am", "3:00am", "4:00am"]

    def is_valid_start_time(self):
        return self.start_time in self.times

    def is_valid_end_time(self):
        return self.end_time in self.times

    def has_babysat_tonight(self):
        return self.babysat_tonight

    def hours_are_not_fractional(self):
        return self.start_time[-4:-2] == "00" and self.end_time[-4:-2] == "00"

    def begin_time_is_before_end_time(self):
        return self.times.index(self.start_time) < self.times.index(self.end_time)

    def family_is_valid(self):
        return self.family in ["a", "b", "c"]

    def can_calculate_nightly_charge(self):
        return (self.is_valid_start_time() and self.is_valid_end_time() and
                not self.has_babysat_tonight() and
                self.hours_are_not_fractional() and
                self.begin_time_is_before_end_time() and
                self.family_is_valid())

    def nightly_charge(self):
        if self.family == "a":
            return self.calculate_family_a()
        elif self.family == "b":
            return self.calculate_family_b()
        else:
            return self.calculate_family_c()

    def calculate_family_a(self):
        hours_before_eleven = None
        hours_after_eleven = None

        if self.times.index(self.end_time) <= self.times.index("11:00pm"):
            hours_before_eleven = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_before_eleven * 15
        else:
            hours_before_eleven = self.times.index("11:00pm") - self.times.index(self.start_time)

        if self.times.index(self.start_time) >= self.times.index("11:00pm"):
            hours_after_eleven = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_after_eleven * 20
        else:
            hours_after_eleven = self.times.index(self.end_time) - self.times.index("11:00pm")

        return hours_before_eleven * 15 + hours_after_eleven * 20

    def calculate_family_c(self):
        hours_before_nine = None
        hours_after_nine = None

        if self.times.index(self.end_time) <= self.times.index("9:00pm"):
            hours_before_nine = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_before_nine * 21
        else:
            hours_before_nine = self.times.index("9:00pm") - self.times.index(self.start_time)

        if self.times.index(self.start_time) >= self.times.index("9:00pm"):
            hours_after_nine = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_after_nine * 15
        else:
            hours_after_nine = self.times.index(self.end_time) - self.times.index("9:00pm")

        return hours_before_nine * 21 + hours_after_nine * 15

    def calculate_family_b(self):
        hours_before_10 = None

        if self.times.index(self.end_time) <= self.times.index("10:00pm"):
            hours_before_10 = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_before_10 * 12
