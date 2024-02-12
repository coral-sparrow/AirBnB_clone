'''
    this is the Review test module
'''

import unittest
from models.review import Review
from datetime import datetime


class Test_ReviewModel(unittest.TestCase):
    ''' unittesting for the base model class '''

    def test_uuid(self):
        ''' test the uuid for the class instance is as expected '''
        bm1 = Review()
        bm2 = Review()

        # bm1 has id?
        self.assertIn('id', bm1.__dict__.keys())
        # id is string?
        self.assertIsInstance(bm1.id, str)
        # uuid is unique for each instance ?
        self.assertNotEqual(bm1.id, bm2.id)


    def test_created_at(self):
        ''' test the created_at attribute '''

        bm = Review()

        # is created_at of type datetime?
        self.assertIsInstance(bm.created_at, datetime)
        # is it in isoformate
        self.assertEqual(bm.created_at,
                         datetime.fromisoformat(bm.to_dict()['created_at']),
                         msg='created_at is not in isoformat in to_dict()')
