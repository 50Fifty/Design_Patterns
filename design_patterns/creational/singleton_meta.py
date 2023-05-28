class SingletonMeta(type):
    """
    Metaclass for Singleton class.
    A metaclass is a blueprint for a class.
    """
    _instances = dict() # Dictionary to store instances of the class.

    def __call__(cls, *args, **kwargs): # __call__ is called when an instance of the class is created.
        """
        This method is called when an instance of the class is created.
        """
        if cls not in cls._instances: # If the class is not in the dictionary, create an instance of the class and store it in the dictionary.
            instance = super().__call__(*args, **kwargs) # Create an instance of the class.
            cls._instances[cls] = instance # Store the instance in the dictionary.
        return cls._instances[cls] # Return the instance of the class.

class Singleton(metaclass=SingletonMeta):
    """
    Singleton class.
        - Inheritable version.
        - e.g. class MyClass(Singleton):
    """
    pass
