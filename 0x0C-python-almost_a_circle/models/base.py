#!/usr/bin/python3
"""
This model contains the Base class
"""
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
            
