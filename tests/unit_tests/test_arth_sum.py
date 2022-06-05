from flaskr.services.series import arithmetic_sum

from unittest import TestCase, main
from unittest.mock import patch


class Arithmetic_sumTest(TestCase):
    def test_arithmetic_sum_zero(self):
        # given
        number = 0
        expected_result = 0
        # when
        result = arithmetic_sum(number)
        # then
        self.assertEqual( expected_result, result)

    def test_arithmetic_sum_negative(self):
        # given
        number = -5
        # then
        self.assertRaises(ValueError, arithmetic_sum, number)

    def test_arithmetic_sum_positive(self):
        # given
        number = 10
        expected_result = 55
        # when
        result = arithmetic_sum(number)
        # then
        self.assertEqual(expected_result, result)

    def test_arithmetic_sum_bigNumber(self):
        # given
        number = 100
        expected_result = 5050
        # when
        result = arithmetic_sum(number)
        # then
        self.assertEqual(expected_result, result)

