# coding:utf-8
import unittest

from app.validators import validate_zipcode


class ValidatorZipCodeTest(unittest.TestCase):

    def test_zipcodes_validator(self):
        """Validates some invalid zipcode scenarios
        """
        # valid zipcode
        self.assertIsNotNone(validate_zipcode('14820000'))
        # too long zip code
        self.assertIsNone(validate_zipcode('148200000'))
        # too short zip code
        self.assertIsNone(validate_zipcode('148200'))
        # not integer zip code
        self.assertIsNone(validate_zipcode('14820-000'))
