"""The Animal class (abstract) should take, as attributes, a name, an age, and a gender.
It should have 2 methods: repr() and make_sound()."""
from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass