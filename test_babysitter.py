import unittest
from babysitter import Babysitter


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        self.a = Babysitter("5:00pm", "3:00am", "a")

    def test_starts_no_earlier_than_5_pm(self):
        self.assertTrue(self.a.is_valid_start_time())

    def test_starts_no_later_than_4_am(self):
        self.assertTrue(self.a.is_valid_end_time())

    def test_only_babysits_for_1_family__per_night(self):
        self.assertFalse(self.a.has_babysat_tonight())

    def test_no_fractional_hours(self):
        self.assertTrue(self.a.hours_are_not_fractional())

    def test_begin_time_is_before_end_time(self):
        self.assertTrue(self.a.begin_time_is_before_end_time())

    def test_family_is_valid(self):
        self.assertTrue(self.a.family_is_valid())

    def test_can_calculate_nightly_charge(self):
        self.assertTrue(self.a.can_calculate_nightly_charge())

    def test_family_a_charges_15_before_11(self):
        a = Babysitter("5:00pm", "6:00pm", "a")
        self.assertEqual(a.nightly_charge(), 15)
        b = Babysitter("5:00pm", "7:00pm", "a")
        self.assertEqual(b.nightly_charge(), 30)
        c = Babysitter("5:00pm", "8:00pm", "a")
        self.assertEqual(c.nightly_charge(), 45)
        d = Babysitter("5:00pm", "11:00pm", "a")
        self.assertEqual(d.nightly_charge(), 90)

    def test_family_a_charges_20_after_11(self):
        a = Babysitter("11:00pm", "12:00am", "a")
        self.assertEqual(a.nightly_charge(), 20)
        b = Babysitter("11:00pm", "1:00am", "a")
        self.assertEqual(b.nightly_charge(), 40)
        c = Babysitter("11:00pm", "3:00am", "a")
        self.assertEqual(c.nightly_charge(), 80)

    def test_family_a_charges_170_for_a_full_night(self):
        a = Babysitter("5:00pm", "3:00am", "a")
        self.assertEqual(a.nightly_charge(), 170)

if __name__ == '__main__':
    unittest.main()
