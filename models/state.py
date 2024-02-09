'''
    State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
        class State
    '''
    name = ''

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
