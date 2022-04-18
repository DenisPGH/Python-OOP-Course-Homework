from abc import ABC,abstractmethod


class Animal(ABC):
    alowed_food=[]
    value_of_dicknes=0


    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.food_eaten=0

    @abstractmethod
    def make_sound(self):
        pass


    def feed(self,type_food):
        if self.__class__.__name__== "Hen":
            self.food_eaten += type_food.quantity
            self.weight += type_food.quantity * self.value_of_dicknes

        elif type_food.__class__.__name__ in self.alowed_food:
            self.food_eaten+=type_food.quantity
            self.weight+= type_food.quantity* self.value_of_dicknes


        else:
            return f"{self.__class__.__name__} does not eat {type_food.__class__.__name__ }!"


"""In the animal.py file, implement the following classes:
•	Animal - the class should be abstract and should have the following attributes:
o	name (string) - passed upon initialization
o	weight (float) - passed upon initialization
o	food_eaten - 0 by default """


class Bird(Animal,ABC):
    def __init__(self, name, weight,wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size
    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


"""
•	Bird - should inherit from the Animal class. 
The class should be abstract and should have wing_size (float) as an additional attribute passed upon
 initialization.
•	Mammal - should inherit from the Animal class. The class should be abstract and
 should have living_region (str) as an additional attribute passed upon initialization.
"""

class Mammal(Animal,ABC):
    def __init__(self, name, weight,living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod # dobavli tezi abs metodi
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

