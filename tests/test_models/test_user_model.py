'''
    this is the User test module
'''

import unittest
from models.user import User
from datetime import datetime


class Test_UserModel(unittest.TestCase):
    ''' unittesting for the User model class '''

    def test_uuid(self):
        ''' test the uuid for the class instance is as expected '''
        bm1 = User()
        bm2 = User()

        # bm1 has id?
        self.assertIn('id', bm1.__dict__.keys())
        # id is string?
        self.assertIsInstance(bm1.id, str)
        # uuid is unique for each instance ?
        self.assertNotEqual(bm1.id, bm2.id)


    def test_created_at(self):
        ''' test the created_at attribute '''

        bm = User()

        # is created_at of type datetime?
        self.assertIsInstance(bm.created_at, datetime)
        # is it in isoformate
        self.assertEqual(bm.created_at,
                         datetime.fromisoformat(bm.to_dict()['created_at']),
                         msg='created_at is not in isoformat in to_dict()')
