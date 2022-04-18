"""" Create a class Hero. It should contain the following attributes:
•	username: string
•	level: int
Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"
"""

class Hero:
    def __init__(self,username,level):
        self.level = level
        self.username=username

    def __str__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"

# h=Hero("H",20)
#
# print(h)
