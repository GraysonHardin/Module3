"""
Program: test_operators_practice
Author: Grayson Hardin
Last date modified: 9/10/2020


This program utilizes various operators and includes testing to show whether they pass or fail.
"""

import unittest


class OperatorTest(unittest.TestCase):
    def test_equal(self):
        actual = 5
        expected = 5
        self.assertTrue(expected == actual)

    def test_not_equal(self):
        actual = 4
        expected = 5
        self.assertTrue(expected != actual)

    def test_greater_than(self):
        actual = 4
        expected = 5
        self.assertTrue(expected > actual)

    def test_less_than(self):
        actual = 6
        expected = 5
        self.assertTrue(expected < actual)

    def test_greater_than_or_equal(self):
        actual = 4
        expected = 5
        self.assertTrue(expected >= actual)

    def test_less_than_or_equal(self):
        actual = 6
        expected = 5
        self.assertTrue(expected <= actual)


if __name__ == '__main__':
    unittest.main()
