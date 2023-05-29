from design_patterns.behavioural.observer import ConcreteObserver, ConcreteSubject

class NotObserver():
    def __init__(self, name) -> None:
        self.__name = name

def test_1_observers_updates_after_subject_state_change():
    subject = ConcreteSubject("Initial State")
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    observer3 = ConcreteObserver("Observer 3")
    observer4 = ConcreteObserver("Observer 4")
    observer5 = ConcreteObserver("Observer 5")

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.attach(observer4)
    subject.attach(observer5)

    subject.set_state("New State")
    assert observer1.get_state() == observer2.get_state() == observer3.get_state() == observer4.get_state() == \
        observer5.get_state() == "New State"

def test_2_attaching_non_observer_type_raises_exception():
    subject = ConcreteSubject("Initial State")
    observer1 = NotObserver("NotObserver 1")

    try:
        subject.attach(observer1)
    except TypeError as e:
        assert str(e) == "observer is not of type: Observer."

def test_3_detaching_non_observer_type_raises_exception():
    subject = ConcreteSubject("Initial State")
    observer1 = NotObserver("NotObserver 1")

    try:
        subject.detach(observer1)
    except TypeError as e:
        assert str(e) == "observer is not of type: Observer."

def test_4_attaching_same_observer_twice_result_in_only_one_instance():
    subject = ConcreteSubject("Initial State")
    observer1 = ConcreteObserver("Observer 1")

    subject.attach(observer1)
    subject.attach(observer1)

    assert len(subject._ConcreteSubject__observers) == 1

def test_5_detaching_observer_not_attached_does_not_raise_exception():
    subject = ConcreteSubject("Initial State")
    observer1 = ConcreteObserver("Observer 1")

    subject.detach(observer1)