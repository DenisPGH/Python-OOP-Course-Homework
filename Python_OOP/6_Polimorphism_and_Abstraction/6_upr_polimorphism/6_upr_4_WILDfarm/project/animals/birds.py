"""In the birds.py file, implement the following classes:
•	Owl
•	Hen

•	Owl - "Hoot Hoot"
•	Hen - "Cluck"
•	Mouse - "Squeak"
•	Dog - "Woof!"
•	Cat - "Meow"
•	Tiger - "ROAR!!!"

"""
from test.animals.animal import Bird


class Owl(Bird):
    alowed_food=["Meat"]
    value_of_dicknes=0.25

    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):
    alowed_food = ["Meat","Fruit","Seed", "Vegetable"]
    value_of_dicknes = 0.35
    def make_sound(self):
        return "Cluck"