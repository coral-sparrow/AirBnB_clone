'''
    Amenity class
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
        class Amenity
    '''

    name = ''

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
