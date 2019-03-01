import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
    def test_starts_no_earlier_than_5_pm(self):
        b = Babysitter(5, 9, "a")
        self.assertEqual(True, b.is_valid_start_time())
