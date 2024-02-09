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
        class_name = type(obj).__name__.split('.')[-1]
        self.__objects[f'{class_name}.{obj.id}'] = obj.to_dict()

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w', encoding='utf8') as db:
            json.dump(self.__objects, db, indent=4)

    def reload(self):
        '''
            deserializes the JSON file
            to __objects (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesnot exist
        '''
        try:
            with open(self.__file_path, 'r', encoding='utf8') as db:
                self.__objects = json.load(db)

        except FileNotFoundError:
            pass
