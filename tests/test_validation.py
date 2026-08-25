import unittest

from activity_generator import validate_date


class ValidateDateTests(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(validate_date("2026-08-25"), "2026-08-25")

    def test_invalid_format(self):
        with self.assertRaises(Exception):
            validate_date("25-08-2026")

    def test_invalid_calendar_date(self):
        with self.assertRaises(Exception):
            validate_date("2026-02-30")


if __name__ == "__main__":
    unittest.main()
