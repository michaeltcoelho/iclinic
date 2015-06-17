# coding:utf-8
import falcon
import logging
from bson import json_util

from .config import Config
from .models import ZipCodeModel
from .postmon import postmon
from .validators import validate_zipcode_on_before, validate_zipcode

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def error_serializer(req, exception):
    """Overrides the default error serializer
    """
    return 'application/json', exception.to_json()


class ZipCodeResource(object):
    """ZipCodeResource
    """
    def __init__(self, model):
        self.model = model

    def on_get(self, req, resp, zip_code=None):
        """Handles a GET / requests
        """
        limit = req.get_param('limit')
        zipcodes = []
        if zip_code:
            if validate_zipcode(zip_code):
                zipcodes = self.model.find_by_zipcode(zip_code)
                logger.info('%s found...' % zipcodes.get('zip_code') or None)
            else:
                raise falcon.HTTPError(
                    falcon.HTTP_400,
                    'The `zip_code` param must be an integer valid zipcode.')
        else:
            zipcodes = self.model.all(limit)
            logger.info('%s resources found limited by %s...' % (
                zipcodes.count(True), limit))
        zipcodes = json_util.dumps(zipcodes)
        resp.body = zipcodes
        resp.status = falcon.HTTP_200

    @falcon.before(validate_zipcode_on_before)
    def on_post(self, req, resp):
        """Handles a POST /zipcode request
        """
        zipcode = req.get_param('zip_code')
        data = self.model.find_by_zipcode(zipcode)
        if data:
            logger.info('%s already exists...' % zipcode)
            resp.status = falcon.HTTP_201
        else:
            logger.info('%s does not exists...' % zipcode)
            rq = postmon.get(zipcode)
            if rq.content:
                try:
                    self.model.insert(rq.json())
                    resp.status = falcon.HTTP_201
                    logger.info('%s zipcode inserted...' % zipcode)
                except Exception as e:
                    logger.error(e)
                    raise falcon.HTTPError(
                        falcon.HTTP_500, 'Error when saving a new data.')
            else:
                logger.info('Postmon response is empty for %s...' % zipcode)
                raise falcon.HTTPError(
                    falcon.HTTP_400,
                    'It wasn`t possible to insert your zipcode. Try it again.')

    def on_delete(self, req, resp, zip_code):
        """Handles a DELETE /zipcode request
        """
        if not validate_zipcode(zip_code):
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'The `zip_code` param must be an integer valid zipcode.')
        else:
            if self.model.find_by_zipcode(zip_code):
                self.model.delete(zip_code)
                resp.status = falcon.HTTP_204
                logger.info('%s was removed...' % zip_code)
            else:
                logger.info('%s doesn`t exists in the database...' % zip_code)
                raise falcon.HTTPError(
                    falcon.HTTP_400,
                    'The zipcode passed does not exists in our database.')


app = application = falcon.API()
app.set_error_serializer(error_serializer)

# instance the resource
zipcode_resource = ZipCodeResource(ZipCodeModel(Config()))

app.add_route('/zipcode', zipcode_resource)
app.add_route('/zipcode/{zip_code}', zipcode_resource)
