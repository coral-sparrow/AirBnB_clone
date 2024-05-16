#!/usr/bin/python3
'''
    basemodel for the Bnb project to inherited from childeren classes.
'''


import uuid
from datetime import datetime


class BaseModel():
    '''
        Base Model to deal with repetitive tasks
        for each instance and generic methods
    '''

    def __init__(self, *args, **kwargs):
        ''' class constructor '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
        if kwargs:
            # self.id = kwargs["id"]
            # self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            # self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            pass
                
    def __str__(self):
        ''' str representation of the class '''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' save method will be updated later '''
        # self.updated_at = datetime.now().isoformat()
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' serializee the object to json format '''
        attributes = self.__dict__.copy()
        attributes['__class__'] = type(self).__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes

if __name__ == "__main__":
    base = BaseModel()
    print(base)
    print(base.to_dict())
