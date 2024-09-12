#!/usr/bin/python3
"""
This module defines FileStorage class for serializing & deserializing objects.
"""

import json
from models import base_model
from models import User
from models import Place
from models import State
from models import City
from models import Amenity
from models import Review


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {k: v.to_dict()
                              for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(globals()[class_name](**value))
        except FileNotFoundError:
            pass