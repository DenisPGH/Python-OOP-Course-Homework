"""In the planet.py file, the class Planet should be implemented. It is an implementation for a planet,
 and it holds information about the items that can be found on its surface.
Structure
The class should have the following attributes:
•	name: str
o	If the name is an empty string or whitespace, raise a ValueError with the
 message: "Planet name cannot be empty string or whitespace!"
•	items: an empty list of strings holding each item that could be found on that planet
Methods
__init__(name: str)
The __init__() method should have a name and items.
"""

class Planet:
    def __init__(self,name):
        self.name = name
        self.items=[] # hold item on the planet

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value=="" or value==" ":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name=value