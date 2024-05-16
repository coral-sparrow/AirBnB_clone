'''
    user class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        class user
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
