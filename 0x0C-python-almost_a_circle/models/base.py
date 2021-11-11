#!/usr/bin/python3
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if (id != None):
            self.id = id
        else:
             __nb_objects+=id
            
