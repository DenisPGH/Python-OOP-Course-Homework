"""In the mammals.py file, implement the following classes:
•	Mouse
•	Dog
•	Cat
•	Tiger

Owl - "Hoot Hoot"
•	Hen - "Cluck"
•	Mouse - "Squeak"
•	Dog - "Woof!"
•	Cat - "Meow"
•	Tiger - "ROAR!!!"
"""
from test.animals.animal import Mammal


class Mouse(Mammal):
    # eat vegetables and fruits
    alowed_food = ["Vegetable", "Fruits"]
    value_of_dicknes = 0.10
    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    alowed_food = ["Meat"]
    value_of_dicknes = 0.40
    def make_sound(self):
        return "Woof!"

class Cat(Mammal):
    # Cats eat vegetables and meat
    alowed_food = ["Vegetable", "Meat"]
    value_of_dicknes = 0.30

    def make_sound(self):
        return "Meow"

class Tiger(Mammal):
    alowed_food = ["Meat"]
    value_of_dicknes = 1
    def make_sound(self):
        return "ROAR!!!"