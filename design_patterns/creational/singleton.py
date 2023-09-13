"""
Singleton: Non-inheritable version.

This is an example of the Singleton design pattern implemented in Python.
The Singleton pattern is used to ensure that only one instance of a class is created.
All further references to objects of the singleton class refer to the same underlying instance.
The Singleton pattern is also referred to as the Singleton Object Creational Pattern.

In this example we have a Singleton class that can only be instantiated once.
Subsequent instantiations will return the same instance.

For the inheritable version, see design_patterns/singleton_meta.py.
"""

class Singleton:
    """
    Singleton class.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name