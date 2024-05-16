'''file storage, serialize python class objects to json'''

import json
import copy
# from models.base_model import BaseModel
# from models.user import User


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
        self.__objects[f'{class_name}.{obj.id}'] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        dict_repr = {}
        for k, v in self.__objects.items():
            dict_repr[k] = copy.deepcopy(v).to_dict()
        with open(self.__file_path, 'w', encoding='utf8') as db:
            json.dump(dict_repr, db, indent=4)

    def reload(self):
        '''
            deserializes the JSON file
            to __objects (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesnot exist
        '''
        try:
            from models.base_model import BaseModel
            from models.user import User

            with open(self.__file_path, 'r', encoding='utf8') as db:
                dict_repr = json.load(db)
            for k in dict_repr.keys():
                class_name = k.split('.')[0]
                if class_name == 'BaseModel':
                    self.__objects[k] = BaseModel(**dict_repr[k])
                elif class_name == 'User':
                    self.__objects[k] = User(**dict_repr[k])

        except FileNotFoundError:
            pass
