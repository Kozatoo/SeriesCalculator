from flaskr.services.series import pentagonal_series

from unittest import TestCase, main
from unittest.mock import patch


class Pentagonal_seriesTest(TestCase):
    def test_pentagonal_series_zero(self):
        # given
        number = 0
        expected_result = 0
        # when
        result = pentagonal_series(number)
        # then
        self.assertEqual( expected_result, result)

    def test_pentagonal_series_negative(self):
        # given
        number = -5
        # then
        self.assertRaises(ValueError, pentagonal_series, number)

    def test_pentagonal_series_positive(self):
        # given
        number = 5
        expected_result = 5
        # when
        result = pentagonal_series(number)
        # then
        self.assertEqual(expected_result, result)

    def test_pentagonal_series_bigNumber(self):
        # given
        number = 100
        # then
        self.assertRaises(ValueError, pentagonal_series, number)
    def test_pentagonal_series_positive2(self):
        # given
        number = 91
        expected_result = 4660046610375530309
        # when
        result = pentagonal_series(number)
        # then
        self.assertEqual(expected_result, result)
