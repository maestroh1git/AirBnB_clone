#!/usr/bin/python3
"""
Contains class base model
"""

import uuid
from datetime import datetime


class BaseModel:
    """Class for all other classes to inherit from"""
    def __init__(self, *args, **kwargs):
        """Method to make instance of Base Model"""
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = kwargs["created_at"]
            if "updated_at" in kwargs:
                self.updated_at = kwargs["updated_at"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}]({:s}){}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].isoformat("T")
        new_dict["updated_at"] = new_dict["updated_at"].isoformat("T")
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
