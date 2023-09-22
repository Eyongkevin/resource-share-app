from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.resources import validators


class TestValidators(TestCase):
    def test_check_rating_range_fail_when_out_of_range(self):
        value = 6

        with self.assertRaises(ValidationError) as err:
            validators.check_rating_range(value)

    def test_check_rating_range_pass_when_in_range(self):
        value = 4

        result = validators.check_rating_range(value)

        self.assertIsNone(result)
