'''
    Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
        class Review
    '''
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
