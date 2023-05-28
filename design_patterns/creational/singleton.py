class Singleton:
    """
    Singleton class.

    For the inheritable version, see design_patterns\singleton_meta.py.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name