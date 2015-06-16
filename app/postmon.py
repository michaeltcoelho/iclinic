# coding:utf-8
import logging
import falcon
import requests
from requests.exceptions import (ConnectionError, RequestException,
                                 ConnectTimeout)
from .config import Config

logger = logging.getLogger(__name__)


class PostMonWrapper(requests.Session):
    """PostManWrapper - A wrapper to communicate to postmon

    Postmon - http://postmon.com.br/
    """
    endpoint = Config.POSTMAN_ENDPOINT

    def get(self, zipcode):
        endpoint = '{}{}'.format(self.endpoint, zipcode)
        try:
            logger.info('Asking postmon for %s...' % zipcode)
            return super(PostMonWrapper, self).get(endpoint)
        except (RequestException, ConnectionError, ConnectTimeout) as e:
            logger.error(e)
            raise falcon.HTTPError(
                falcon.HTTP_500, 'Fail when consuming an external resource.')

postmon = PostMonWrapper()
