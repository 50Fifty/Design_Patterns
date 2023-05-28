from design_patterns.singleton import Singleton

def test_1_same_singleton_instance():
    """
    Creating instances of Singleton should return the same object.
    """
    instance1 = Singleton("Instance 1")
    instance2 = Singleton("Instance 2")
    instance3 = Singleton("Instance 3")
    instance4 = Singleton("Instance 4")
    instance5 = Singleton("Instance 5")
    assert instance1 is instance2 is instance3 is instance4 is instance5

def test_2_same_singleton_name():
    """
    Creating instances of Singleton should have the same name.
    """
    instance1 = Singleton("Instance 1")
    instance2 = Singleton("Instance 2")
    instance3 = Singleton("Instance 3")
    instance4 = Singleton("Instance 4")
    instance5 = Singleton("Instance 5")
    assert instance1.name == instance2.name == instance3.name == instance4.name == instance5.name == "Instance 1"

