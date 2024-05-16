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
<<<<<<< HEAD
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
=======
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            from models.city import City
            from models.state import State

            with open(self.__file_path, 'r', encoding='utf8') as db:
                dict_repr = json.load(db)
            for k in dict_repr.keys():
                class_name = k.split('.')[0]
                if class_name == 'BaseModel':
                    self.__objects[k] = BaseModel(**dict_repr[k])
                elif class_name == 'User':
                    self.__objects[k] = User(**dict_repr[k])
                elif class_name == 'Amenity':
                    self.__objects[k] = Amenity(**dict_repr[k])
                elif class_name == 'Place':
                    self.__objects[k] = Place(**dict_repr[k])
                elif class_name == 'Review':
                    self.__objects[k] = Review(**dict_repr[k])
                elif class_name == 'City':
                    self.__objects[k] = City(**dict_repr[k])
                elif class_name == 'State':
                    self.__objects[k] = State(**dict_repr[k])

>>>>>>> adeac056af467435b2f9aff9a2288ea6793d0736
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

