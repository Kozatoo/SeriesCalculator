from flaskr.services.series import fibonacci

from unittest import TestCase, main
from unittest.mock import patch


class FibonacciTest(TestCase):
    def test_fibonacci_zero(self):
        # given
        number = 0
        expected_result = 0
        # when
        result = fibonacci(number)
        # then
        self.assertEqual( expected_result, result)

    def test_fibonacci_negative(self):
        # given
        number = -5
        # then
        self.assertRaises(ValueError, fibonacci, number)

    def test_fibonacci_positive(self):
        # given
        number = 5
        expected_result = 5
        # when
        result = fibonacci(number)
        # then
        self.assertEqual(expected_result, result)

    def test_fibonacci_bigNumber(self):
        # given
        number = 100
        # then
        self.assertRaises(ValueError, fibonacci, number)
    def test_fibonacci_positive2(self):
        # given
        number = 91
        expected_result = 4660046610375530309
        # when
        result = fibonacci(number)
        # then
        self.assertEqual(expected_result, result)
