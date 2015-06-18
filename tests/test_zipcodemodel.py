# coding:utf-8
import unittest

from app.config import Config
from app.models import ZipCodeModel


class ZipCodeModelTest(unittest.TestCase):

    def setUp(self):
        self.model = ZipCodeModel(Config())
        self.items = [{
            'city': 'Araraquara',
            'neighborhood': 'Centro',
            'state': 'SP',
            'address': 'Rua 9 de Julho',
            'zip_code': 14800409
        }, {
            'city': 'Araraquara',
            'neighborhood': 'Centro',
            'state': 'SP',
            'address': 'Avenida São José',
            'zip_code': 14800410
        }, {
            'city': 'Araraquara',
            'neighborhood': 'Centro',
            'state': 'SP',
            'address': 'Avenida Djalma Dutra',
            'zip_code': 14800400
        }]
        for item in self.items:
            self.model.insert(item)

    def test_1_insert(self):
        """Insert a zipcode data

        should return a not None object
        """
        zipcode = self.model.insert({
            'zip_code': 14820000,
            'address': 'Rua Nove de Julho',
            'neighborhood': 'Centro',
            'state': 'SP',
            'city': 'Araraquara'
        })
        self.assertIsNotNone(zipcode)

    def test_2_delete(self):
        """Delete an existing zipcode

        should return a json object with an `ok` key
        and its value equals 1
        """
        zipcode = self.model.delete(14820000)
        self.assertEqual(zipcode['ok'], 1)

    def test_3_all_without_limit(self):
        """Get all items from the collection

        should return a list of 3 items
        """
        zipcodes = self.model.all()
        self.assertEqual(zipcodes.count(), 27)

    def test_4_all_with_limit(self):
        """Get all items from the collection with a limit

        should return a list of 2 items
        """
        zipcodes = self.model.all(limit=2)
        self.assertEqual(zipcodes.count(True), 2)
