"""
Observer 

This is an example of the Observer design pattern implemented in Python.
The Observer pattern is used to allow an object to publish changes to its state.
Other objects subscribe via the Subject's attach() method to be immediately notified of any changes.

In this example we have a Subject class (Publisher) that has a state that can be modified.
The Subject also has a list of all the Observers (Subscribers) that are subscribed to it.
When the Subject's state is modified, it notifies all its Observers.
The Observers can then query the Subject for its state via the get_state() method.

Reference: Design Patterns: Elements of Reusable Object-Oriented Software
"""

from abc import ABC, abstractmethod

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass

class Observer(ABC):
    """
    The Observer interface declares a set of methods for updating subscribers.
    """

    @abstractmethod
    def update(self):
        pass

class ConcreteSubject(Subject):
    """
    Concrete Subjects own some important state and notifies observers when the state changes.
    """

    def __init__(self, state) -> None:
        super().__init__()
        self.__subject_state = state
        self.__observers = []

    def attach(self, observer: Observer):
        if not isinstance(observer, Observer):
            raise TypeError("observer is not of type: Observer.")
        if observer not in self.__observers:
            observer.update(self.__subject_state)
            self.__observers.append(observer)
            
    def detach(self, observer: Observer):
        if not isinstance(observer, Observer):
            raise TypeError("observer is not of type: Observer.")
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self):
        for o in self.__observers:
            if not isinstance(o, Observer):
                raise TypeError("o is not of type: Observer.")
            o.update(self.__subject_state)

    def get_state(self):
        return self.__subject_state
    
    def set_state(self, state):
        self.__subject_state = state
        self.notify()

class ConcreteObserver(Observer):
    """
    Concrete Observers react to the updates issued by the Subject they had been attached to.
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.__name = name
        self.__observer_state = None

    def update(self, new_state):
        # old_state = self.__observer_state
        self.__observer_state = new_state
        # print(f"{self.__name}: Subject state has changed from {old_state} to {self.__observer_state}")

    def get_state(self):
        return self.__observer_state