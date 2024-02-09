'''
    basemodel for the Bnb project to inherited from childeren classes.
'''


import uuid
from datetime import datetime
from . import storage


class BaseModel():
    '''
        Base Model to deal with repetitive tasks
        for each instance and generic methods
    '''

    def __init__(self, *args, **kwargs):
        ''' class constructor '''

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue

                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(v))
                    # self.k = datetime.fromisoformat(v)
                else:
                    setattr(self, k, v)

    def __str__(self) -> str:
        ''' str representation of the class '''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' save method will be updated later '''
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        ''' serializee the object to json format '''
        attributes = self.__dict__
        attributes['__class__'] = type(self).__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes
