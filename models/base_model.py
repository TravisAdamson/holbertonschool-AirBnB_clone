#!/usr/bin/python3
# base_model.py
"""Defines a new class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """Creates an new BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Creates the string representation of the obj"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """Updates most recent change time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary representation of the obj"""
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
