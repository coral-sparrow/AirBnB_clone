#!/usr/bin/python3
'''file storage, serialize python class objects to json'''


from models.base_model import BaseModel
from models.user import User
import json


class FileStorage():
    '''file storage, serialize python class objects to json'''

    __file_path = 'file.json'
    __objects = {}
    
    classes = {
      "BaseModel": BaseModel,
      "User": User
    }

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        dict_temp = {}
        for k, v in self.__objects.items():
            dict_temp[k] = v.to_dict()
        with open(self.__file_path, 'w') as db:
            json.dump(dict_temp, db, indent=4)

    def reload(self):
        '''
            deserializes the JSON file
            to __objects (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesnot exist
        '''
        try:
            with open(self.__file_path, 'r') as db:
                dict_temp = json.load(db)
            for k in dict_temp.keys():
                class_name = k.split('.')[0]
                obj = self.classes[class_name](**dict_temp[k])
                # if class_name == 'BaseModel':
                #     self.__objects[k] = BaseModel(**dict_temp[k])
                # elif class_name == 'User':
                #     self.__objects[k] = User(**dict_temp[k])
                self.__objects[k] = obj
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    base = BaseModel()
    print(base)
    print(base.to_dict())
    storage = FileStorage()
    storage.reload()
    
    storage.new(base)
    storage.save()

