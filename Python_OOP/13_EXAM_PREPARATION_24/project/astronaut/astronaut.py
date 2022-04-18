"""
•	оxygen: int
o	The oxygen of an astronaut in units
•	backpack: an empty list
o	In the backpack, each astronaut will collect items while on a mission
Methods
__init__(name: str, oxygen: int)
The __init__ method should have a name, a given amount of oxygen, and a backpack.
breathe()
Each time an astronaut takes a breath, their oxygen decreases by 10 units.
 Note: some types of astronauts need more oxygen units while breathing.

increase_oxygen(amount: int)
Increases the oxygen with the given amount.
"""
from abc import  ABC,abstractmethod
class Astronaut(ABC):
    DEFAULT_BREATH_VALUE=10
    @abstractmethod
    def __init__(self,name,oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack=[] # collect items while on a mission Methods

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value=="" or value==" ":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name=value

    def breathe(self):
        self.oxygen-=self.DEFAULT_BREATH_VALUE

    def increase_oxygen(self,amount: int):
        self.oxygen+=amount



