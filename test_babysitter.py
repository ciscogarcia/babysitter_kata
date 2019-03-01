import unittest
from babysitter import Babysitter


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        self.b = Babysitter("5:00pm", "9:00pm", "a")
    
    def test_starts_no_earlier_than_5_pm(self):
        self.assertEqual(True, self.b.is_valid_start_time())

    def test_starts_no_later_than_4_am(self):
        self.assertEqual(True, self.b.is_valid_end_time())

    def test_only_babysits_for_1_family__per_night(self):
        self.assertEqual(False, self.b.has_not_babysat_tonight())
        
