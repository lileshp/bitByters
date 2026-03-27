'''
Abstraction:
    Abstract class
    Abstract method

    python use a module:
    
    from abc import ABC, abstractmethod

    
    # A abstract class with 1 or more abstractmethod
    # we cannot create an object of abstract class.
    # all abstract methods only declare without implementation
    # abstract method should be redeclare in child class as a normal method

'''
from abc import ABC, abstractmethod

class Car(ABC):
    def driving_side(self):
        pass
    
    @abstractmethod
    def fuel(self):
        pass
    
    @abstractmethod # decorator
    def wheel(self):
        pass

    def color(self):
        pass

class Tata(Car):
    def fuel(self):
        pass
    def wheel(self):
        pass
punch = Tata()


'''

'''