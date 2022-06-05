from flaskr.services.series import caterer_sequence

from unittest import TestCase, main
from unittest.mock import patch


class Caterer_sequenceTest(TestCase):
    def test_caterer_sequence_zero(self):
        # given
        number = 0
        expected_result = 1
        # when
        result = caterer_sequence(number)
        # then
        self.assertEqual( expected_result, result)
    def test_caterer_sequence_one(self):
        # given
        number = 1
        expected_result = 2
        # when
        result = caterer_sequence(number)
        # then
        self.assertEqual( expected_result, result)
    def test_caterer_sequence_seven(self):
        # given
        number = 3
        expected_result = 7
        # when
        result = caterer_sequence(number)
        # then
        self.assertEqual( expected_result, result)
    def test_caterer_sequence_bigNumber(self):
        # given
        number = 70
        expected_result = 2486
        # when
        result = caterer_sequence(number)
        # then
        self.assertEqual( expected_result, result)

    def test_caterer_sequence_negative(self):
        # given
        number = -5
        # then
        self.assertRaises(ValueError, caterer_sequence, number)

