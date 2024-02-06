import uuid
from datetime import datetime

class BaseModel():
    '''Base Model to deal with repetitive tasks for each instance and generic methods'''
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        attributes = self.__dict__
        attributes['__class__'] = type(self).__name__
        attributes['created_at'] =  attributes['created_at'].isoformat()
        attributes['updated_at'] =  attributes['updated_at'].isoformat()
        return attributes
