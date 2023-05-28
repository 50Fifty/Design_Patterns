from design_patterns.singleton_meta import Singleton

class MySingleton(Singleton):
    """
    Class with Singleton properties.
    """
    def __init__(self, name):
        self.name = name


def test_1_same_singleton_instance():
    """
    Creating instances of MySingleton should return the same object.
    """
    instance1 = MySingleton("Instance 1")
    instance2 = MySingleton("Instance 2")
    instance3 = MySingleton("Instance 3")
    instance4 = MySingleton("Instance 4")
    instance5 = MySingleton("Instance 5")
    assert instance1 is instance2 is instance3 is instance4 is instance5

def test_2_same_singleton_name():
    """
    Creating instances of MySingleton should have the same name.
    """
    instance1 = MySingleton("Instance 1")
    instance2 = MySingleton("Instance 2")
    instance3 = MySingleton("Instance 3")
    instance4 = MySingleton("Instance 4")
    instance5 = MySingleton("Instance 5")
    assert instance1.name == instance2.name == instance3.name == instance4.name == instance5.name == "Instance 1"