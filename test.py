import unittest
from unittest import TestCase

from main import sum_numbers


class TestMain(TestCase):
    def test_sum_number(self):
        self.assertEqual(sum_numbers(1, 2), 3)
        self.assertEqual(sum_numbers(1, 3), 4)


if __name__ == '__main__':
    unittest.main()
