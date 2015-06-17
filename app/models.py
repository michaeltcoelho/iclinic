# coding:utf-8
from pymongo import MongoClient
from pymongo.database import Database


class ZipCodeModel(object):
    """ZipCodeModel
    """
    def __init__(self, config):
        self.db = Database(MongoClient(config.MONGO_HOST, config.MONGO_PORT),
                           config.MONGO_DB_NAME)
        self.zipcodes = self.db.zipcodes

    def insert(self, data):
        """Makes an insertion in mongodb
        """
        return self.zipcodes.insert({
            'zip_code': data.get('cep'),
            'address': data.get('logradouro'),
            'neighborhood': data.get('bairro'),
            'city': data.get('cidade'),
            'state': data.get('estado')
        })

    def delete(self, zipcode):
        """Makes a deletion in mongodb
        """
        return self.zipcodes.remove({"zip_code": zipcode})

    def all(self, limit=None):
        """Returns a list of data with a given limit when it is passed,
        when not, return all data in the collection
        """
        if not limit:
            return self.zipcodes.find({}, {'_id': False})
        return self.zipcodes.find({}, {'_id': False}).limit(int(limit))

    def find_by_zipcode(self, zipcode):
        """Returns a document by zip_code
        """
        return self.zipcodes.find_one({"zip_code": zipcode}, {'_id': False})
