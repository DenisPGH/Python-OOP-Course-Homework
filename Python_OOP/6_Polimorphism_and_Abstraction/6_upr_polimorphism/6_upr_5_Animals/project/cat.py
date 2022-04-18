"""The Cat class should inherit and implement the Animal class. Its repr() method should
return "This is {name}. {name} is a {age} year old {gender} {class}". The cat sound, "Meow meow!"."""
from test.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)


    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a" \
               f" {self.age} year old {self.gender} {self.__class__.__name__}"
