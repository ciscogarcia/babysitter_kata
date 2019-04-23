class Babysitter():
    """Class to determine if we can charge for a night, and calculate how much we should be paid"""
    def __init__(self, start_time, end_time, family):
        self.start_time = start_time
        self.end_time = end_time
        self.family = family
        self.babysat_tonight = False
        self.times = ["5:00pm", "6:00pm", "7:00pm", "8:00pm", "9:00pm", "10:00pm", "11:00pm", "12:00am", "1:00am", "2:00am", "3:00am", "4:00am"]

    def is_valid_start_time(self):
        """Checks to see if the start time is valid"""
        return self.start_time in self.times

    def is_valid_end_time(self):
        """Checks to see if the end time is valid"""
        return self.end_time in self.times

    def has_babysat_tonight(self):
        """Checks to see if we have already babysat for a family tonight"""
        return self.babysat_tonight

    def hours_are_not_fractional(self):
        """Checke to see that we are not charging for partial hours"""
        return self.start_time[-4:-2] == "00" and self.end_time[-4:-2] == "00"

    def begin_time_is_before_end_time(self):
        """Checks to make sure that our start time is chronologically before our end time"""
        return self.times.index(self.start_time) < self.times.index(self.end_time)

    def family_is_valid(self):
        """Make sure the family is on valid"""
        return self.family in ["a", "b", "c"]

    def can_calculate_nightly_charge(self):
        """Run through all of our validity checks"""
        return (self.is_valid_start_time() and self.is_valid_end_time() and
                not self.has_babysat_tonight() and
                self.hours_are_not_fractional() and
                self.begin_time_is_before_end_time() and
                self.family_is_valid())

    def nightly_charge(self):
        """Calculate the what we should be paid for an evening"""
        if self.family == "a":
            return self.calculate_family_a()
        elif self.family == "b":
            return self.calculate_family_b()
        else:
            return self.calculate_family_c()

    def calculate_family_a(self):
        """Calculations specific to family a"""
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
        """Calculations specific to family c"""
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
        """Calculations specific to family b"""
        hours_before_10 = 0
        hours_after_12 = 0
        hours_between_10_and_12 = 0

        if self.times.index(self.end_time) <= self.times.index("10:00pm"):
            hours_before_10 = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_before_10 * 12
        elif self.times.index(self.start_time) < self.times.index("10:00pm"):
            hours_before_10 = self.times.index("10:00pm") - self.times.index(self.start_time)

        if self.times.index(self.start_time) >= self.times.index("12:00am"):
            hours_after_12 = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_after_12 * 16
        elif self.times.index(self.end_time) >= self.times.index("12:00am"):
            hours_after_12 = self.times.index(self.end_time) - self.times.index("12:00am")

        if (self.times.index(self.start_time) >= self.times.index("10:00pm") and
            self.times.index(self.end_time) <= self.times.index("12:00am")):
            hours_between_10_and_12 = self.times.index(self.end_time) - self.times.index(self.start_time)
            return hours_between_10_and_12 * 8

        if (self.times.index(self.start_time) <= self.times.index("10:00pm") and
            self.times.index(self.end_time) >= self.times.index("12:00am")):
            hours_between_10_and_12 = 2

        if (self.times.index(self.start_time) <= self.times.index("10:00pm") and
            self.times.index(self.end_time) > self.times.index("10:00pm") and
            self.times.index(self.end_time) < self.times.index("12:00am")):
            hours_between_10_and_12 = 1

        if (self.times.index(self.start_time) > self.times.index("10:00pm") and
            self.times.index(self.start_time) <= self.times.index("12:00am") and
            self.times.index(self.end_time) >= self.times.index("12:00am")):
            hours_between_10_and_12 = 1

        return hours_before_10 * 12 + hours_after_12 * 16 + hours_between_10_and_12 * 8


def usage():
    print("""
    python babysitter.py start end family

    start\tstart time between 5:00pm and 4:00am.\t ex. 7:00pm
    end\t\tendtime between 5:00pm and 4:00am.\t ex. 1:00am
    family\tfamily a, b, or c.\t\t\t ex. c
""")


if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser(description="Get start time, end time, and family")
    parser.add_argument("start_time", type=str)
    parser.add_argument("end_time", type=str)
    parser.add_argument("family", type=str)
    args = parser.parse_args()

    babysitter = Babysitter(args.start_time, args.end_time, args.family)
    if babysitter.can_calculate_nightly_charge():
        print("You should charge ${} for family {} if you started at {} and ended at {}".format(babysitter.nightly_charge(), babysitter.family, babysitter.start_time, babysitter.end_time))
    else:
        usage()
