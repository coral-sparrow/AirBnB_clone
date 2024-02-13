'''
    this is the BaseModel test module
'''

import unittest
from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    ''' unittesting for the base model class '''

    def test_all(self):
        ''' test the uuid for the class instance is as expected '''
        # storage = FileStorage()

        bm1 = BaseModel()
        bm2 = BaseModel()

        # bm1 has id?
        self.assertTrue(len(storage.all()) >= 2)
