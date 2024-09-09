#!/usr/bin/python3
"""
This module defines the BaseModel class, which is the base class for all
models in the AirBnB clone project.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        
        Args:
            *args: Not used.
            **kwargs: Dictionary of attributes to initialize the instance with.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    
    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
