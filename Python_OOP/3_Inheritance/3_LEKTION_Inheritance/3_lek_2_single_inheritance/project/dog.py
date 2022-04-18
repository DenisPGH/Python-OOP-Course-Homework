"""In a folder called project_ create two files: animal.py and dog.py:
•	In the animal.py file, create a class called Animal with a single method eat() that returns: "eating…".
•	In the dog.py file, create a class called Dog with a single method bark() that returns: "barking…".
The Dog should inherit from Animal.
Submit in Judge a zip file of the folder project_.

"""
from .animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."
