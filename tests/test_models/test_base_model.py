'''
    this is the BaseModel test module
'''

import unittest 
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):
    ''' unittesting for the base model class '''

    def test_uuid(self):
        ''' test the uuid for the class instance is as expected '''
        bm1 = BaseModel()
        bm2 = BaseModel()

        # bm1 has id?
        self.assertIn('id', bm1.__dict__.keys())
        # id is string?
        self.assertIsInstance(bm1.id, str)
        # uuid is unique for each instance ?
        self.assertNotEqual(bm1.id, bm2.id)

    def test_todict(self):
        ''' test if to_dict() is as expected '''

        bm = BaseModel()

        # is all attributes is out?
        self.assertTrue(set(bm.to_dict().keys()).issubset(set(['id', '__class__', 'updated_at', 'created_at', ])))
        # created_at is converted to str?
        # self.assertIsInstance(bm.to_dict()['created_at'], str, msg = "created at is not str in to_dict() output")
        # # updated_at is converted to str?
        # self.assertIsInstance(bm.to_dict()['update_at'], str, msg = "updated_at at is not str in to_dict() output")

    def test_created_at(self):
        ''' test the created_at attribute '''

        bm = BaseModel()

        # is created_at of type datetime?
        self.assertIsInstance(bm.created_at, datetime)
        # is it in isoformate
        self.assertEqual(bm.created_at, datetime.fromisoformat(bm.to_dict()['created_at']), msg='created_at is not in isoformat in to_dict()')