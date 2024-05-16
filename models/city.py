'''
    City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        class City
    '''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
