'''file storage, serialize python class objects to json'''

import json


class FileStorage():
    '''file storage, serialize python class objects to json'''
    
    __file_path = 'db.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects
    
    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[f'{type(obj)}.{obj.id}'] = obj

    def save(self): 
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'a') as db:
            json.dump(self.__objects, db)
            # for id, obj in self.__objects.items():
            #     obj_dict_format = obj.to_dict()