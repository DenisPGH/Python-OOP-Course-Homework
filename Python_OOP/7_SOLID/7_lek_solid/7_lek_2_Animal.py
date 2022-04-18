"""Refactor the provided code, so you do not need to make any changes
 in it when you want to add new species to the animals' list"""

class Animal:
    SPECIES=""
    SOUND=""
    def __init__(self):
        pass

    def make_sound(self):
        return self.SOUND


    def get_species(self):
        return self.SPECIES

class Dog(Animal):
    SPECIES = "Dog"
    SOUND = "Ruf Ruf"

class Cat(Animal):
    SPECIES = "Cat"
    SOUND = "Meow"

class Tiger(Animal):
    SPECIES = "Catttt"
    SOUND = "RRRRRRRRRR"


class Animal_list:
    """ this function store all animals to the list"""
    def __init__(self):
        self.all_animals=[]

    def store_animal(self,animal):
        self.all_animals.append(animal)

    def __getitem__(self, item):
        return self.all_animals[item]



def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


ani=Animal_list()
ani.store_animal(Tiger())
ani.store_animal(Cat())
ani.store_animal(Dog())

animal_sound(ani)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
