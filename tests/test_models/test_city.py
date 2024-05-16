'''
    this is the BaseModel test module
'''

import unittest
from models.city import City
from datetime import datetime


class Test_CityModel(unittest.TestCase):
    ''' unittesting for the City model class '''

    def test_uuid(self):
        ''' test the uuid for the class instance is as expected '''
        bm1 = City()
        bm2 = City()

        # bm1 has id?
        self.assertIn('id', bm1.__dict__.keys())
        # id is string?
        self.assertIsInstance(bm1.id, str)
        # uuid is unique for each instance ?
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        ''' test the created_at attribute '''

        bm = City()

        # is created_at of type datetime?
        self.assertIsInstance(bm.created_at, datetime)
        # is it in isoformate
        self.assertEqual(bm.created_at,
                         datetime.fromisoformat(bm.to_dict()['created_at']),
                         msg='created_at is not in isoformat in to_dict()')
