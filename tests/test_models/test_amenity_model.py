'''
    this is the BaseModel test module
'''

import unittest
from models.amenity import Amenity


class Test_AmenityModel(unittest.TestCase):
    ''' unittesting for the base model class '''

    def test_uuid(self):
        ''' test the uuid for the class instance is as expected '''
        bm1 = Amenity()
        bm2 = Amenity()

        # bm1 has id?
        self.assertIn('id', bm1.__dict__.keys())
        # id is string?
        self.assertIsInstance(bm1.id, str)
        # uuid is unique for each instance ?
        self.assertNotEqual(bm1.id, bm2.id)
