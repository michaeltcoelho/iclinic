# coding:utf-8
import unittest
import requests


class ZipCodeResourceTest(unittest.TestCase):

    def setUp(self):
        self.endpoint = 'http://127.0.0.1:8000/zipcode'

    def test_1_post_resources(self):
        """Makes a POST /zipcode to insert zipcodes

        should return a status code 201 on each POST request
        """
        zipcodes = [
            14820000, 14800409, 14800410, 14800400, 14800390, 14800380,
            14800375, 14800370, 14800369, 14800417, 14800419, 14800432,
            14800460, 14800479, 14800480, 14800489, 14800085, 14800080
        ]
        for zipcode in zipcodes:
            req = requests.post(self.endpoint, data={'zip_code': zipcode})
            self.assertEqual(req.status_code, 201)

    def test_2_post_resource_with_invalid_zipcode(self):
        """Makes a POST /zipcode to insert a zipcode

        should return a status code 400 and the specific message
        The `zip_code` param must be an integer valid zipcode with 8 digits.
        """
        req = requests.post(self.endpoint, data={'zip_code': '14820-000'})
        data = req.json()
        self.assertEqual(req.status_code, 400)
        self.assertEqual(
            data['title'],
            u'The `zip_code` param must be an integer valid zipcode '
            u'with 8 digits.')

    def test_3_post_resource_with_a_too_long_zipcode(self):
        """Makes a POST /zipcode to insert a zipcode

        should return a status code 400 and the specific message
        The `zip_code` param must be an integer valid zipcode with 8 digits.
        """
        req = requests.post(self.endpoint, data={'zip_code': 148200000})
        data = req.json()
        self.assertEqual(req.status_code, 400)
        self.assertEqual(
            data['title'],
            u'The `zip_code` param must be an integer valid zipcode '
            u'with 8 digits.')

    def test_4_get_resources_without_limit(self):
        """Makes a GET /zipcode without a limit query string

        should return 18 json objects and status code 200
        """
        req = requests.get(self.endpoint)
        self.assertEqual(len(req.json()), 18)
        self.assertEqual(req.status_code, 200)

    def test_5_get_resources_with_limit_of_5_items(self):
        """Makes a GET /zipcode with a limit of 5 items

        should return 5 json objects and status code 200
        """
        req = requests.get(self.endpoint, params={'limit': 5})
        self.assertEqual(len(req.json()), 5)
        self.assertEqual(req.status_code, 200)

    def test_6_get_a_resource_by_zipcode(self):
        """Makes a GET /zipcode with a zip_code

        should return 1 json object and status code 200
        """
        req = requests.get('{}/{}'.format(self.endpoint, 14800080))
        resource = req.json()

        self.assertEqual(req.status_code, 200)
        self.assertEqual(resource['city'], u'Araraquara')
        self.assertEqual(resource['neighborhood'], u'Jardim Vitória')
        self.assertEqual(resource['address'], 'Avenida Durval Ferreira')
        self.assertEqual(resource['state'], 'SP')
        self.assertEqual(resource['zip_code'], '14800080')

    def test_7_get_a_resource_with_an_invalid_zipcode(self):
        """Makes a GET /zipcode with an invalid zip_code

        should return a status code 400 and the specific message
        The `zip_code` param must be an integer valid zipcode with 8 digits.
        """
        req = requests.get('{}/{}'.format(self.endpoint, '12332-000'))
        data = req.json()
        self.assertEqual(req.status_code, 400)
        self.assertEqual(
            data['title'],
            u'The `zip_code` param must be an integer valid zipcode '
            u'with 8 digits.')

    def test_8_get_a_resource_with_a_too_long_zipcode(self):
        """Makes a GET /zipcode with an invalid zip_code

        should return a status code 400 and the specific message
        The `zip_code` param must be an integer valid zipcode with 8 digits.
        """
        req = requests.get('{}/{}'.format(self.endpoint, 148200000))
        data = req.json()
        self.assertEqual(req.status_code, 400)
        self.assertEqual(
            data['title'],
            u'The `zip_code` param must be an integer valid zipcode '
            u'with 8 digits.')

    def test_9_delete_a_resource(self):
        """Makes a DELETE /zipcode request

        should delete a resource and return status code 204
        """
        req = requests.delete('{}/{}'.format(self.endpoint, 14820000))
        self.assertEqual(req.status_code, 204)

    def test_10_delete_with_an_invalid_resource(self):
        """Makes a DELETE /zipcode request with an invalid zipcode

        should return a status code 400 and the specific message
        The `zip_code` param must be an integer valid zipcode with 8 digits.
        """
        req = requests.delete('{}/{}'.format(self.endpoint, '148200-000'))
        data = req.json()
        self.assertEqual(req.status_code, 400)
        self.assertEqual(
            data['title'],
            u'The `zip_code` param must be an integer valid zipcode '
            u'with 8 digits.')
