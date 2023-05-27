from design_patterns.singleton import Singleton

class ChildClass1(Singleton):
    """
    ChildClass1 that inherits from Singleton.
    It has the property that all instances of ChildClass are the same object.
    """
    def __init__(self, name):
        self.name = name

class ChildClass2(Singleton):
    """
    ChildClass2 that inherits from Singleton.
    It has the property that all instances of ChildClass are the same object.
    """
    def __init__(self, name):
        self.name = name

def test_Singleton():
    """
    Function to test Singleton.
        - Only one instance should be created when an object is instantiated twice.
    """
    instance1 = ChildClass1("Instance 1")
    instance2 = ChildClass1("Instance 2")
    assert instance1 is instance2

# if __name__ == "__main__":
#     # Creating instances of ChildClass1 and ChildClass2.
#     instance1 = ChildClass1("Instance 1")
#     instance2 = ChildClass1("Instance 2")
#     instance3 = ChildClass2("Instance 3")

#     print(f"Are instance1 and instance2 the same object: {instance1 is instance2}") # Output: True
#     print(f"Are instance1 and instance3 the same object: {instance1 is instance3}") # Output: False
#     print(f"Are instance2 and instance3 the same object: {instance2 is instance3}") # Output: False
#     print(f"instance1 name: {instance1.name}") # Output: Instance 1
#     print(f"instance2 name: {instance2.name}") # Output: Instance 1
#     print(f"instance3 name: {instance3.name}") # Output: Instance 3
