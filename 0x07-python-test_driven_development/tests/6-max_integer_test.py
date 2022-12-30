#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Test the max_integer function
    """

    def test_signed_and_unsigned_int(self):
        """
            Test for positive and negative integers
        """
        self.assertEqual(max_integer([1, 4, 3, 7, 10]), 10)
        self.assertEqual(max_integer([-1, -4, -3, -7, -10]), -1)
        self.assertEqual(max_integer([-1, -4, 3, -7, -10]), 3)

    def test_float(self):
        """
            Test for floats
        """
        self.assertEqual(max_integer([1.0, 4.0, 3.0, 7.0, 10.0]), 10.0)
        self.assertEqual(max_integer([-1.0, -4.0, -3.0, -7.0, -10.0]), -1.0)

    def test_int_and_float(self):
        """
            Test for a list containing both int and float
        """
        self.assertEqual(max_integer([1, 4.0, 3, 7, 10.0]), 10.0)

    def test_one_element(self):
        """
            Test for just one element in list
        """
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """
            Test for no argument or empty list
        """
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)

    def test_non_int_arg(self):
        """
            Test for mixed list
        """
        with self.assertRaises(TypeError):
            max_integer([1, 4, "Yello!", 7, 10])

if __name__ == "__main__":
    unittest.main()
