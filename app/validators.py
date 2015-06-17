# coding:utf-8
import falcon
import re


def validate_zipcode_on_before(req, resp, params):
    """validate_zipcode - validates a zipcode before each requests
    that requires a zipcode
    """
    zipcode = req.get_param('zip_code') or None
    if not zipcode:
        raise falcon.HTTPError(
            falcon.HTTP_400, 'A `zip_code` param must be informed.')
    if not validate_zipcode(zipcode):
        raise falcon.HTTPError(
            falcon.HTTP_400,
            'The `zip_code` param must be an integer valid zipcode '
            'with 8 digits.')


def validate_zipcode(zipcode):
    """validate_zipcode - validates a zipcode number
    """
    return re.match(r'^[0-9]{8}$', zipcode)
