from flaskr.services.series import square_numbers

from unittest import TestCase, main
from unittest.mock import patch


class Square_numbersTest(TestCase):
    def test_square_numbers_zero(self):
        # given
        number = 0
        expected_result = 0
        # when
        result = square_numbers(number)
        # then
        self.assertEqual( expected_result, result)

    def test_square_numbers_negative(self):
        # given
        number = -5
        expected_result=25
        #when
        result = square_numbers(number)
        # then
        self.assertEqual(expected_result,result)

    def test_square_numbers_positive(self):
        # given
        number = 5
        expected_result = 25
        # when
        result = square_numbers(number)
        # then
        self.assertEqual(expected_result, result)

    def test_square_numbers_bigNumber(self):
        # given
        number = 1001
        expected_result = 1002001
        # when
        result = square_numbers(number)
        # then
        self.assertEqual(expected_result, result)
