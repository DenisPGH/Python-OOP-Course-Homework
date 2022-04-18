"""In the astronaut_repository.py file, the class AstronautRepository should be implemented.
 It is a repository for the astronauts that are on the Space Station.
Structure
The class should have the following attributes:
•	astronauts: an empty list of astronauts
Methods
__init__()
The __init__ method should have astronauts.
add(astronaut: Astronaut)
•	Adds an astronaut.
remove(astronaut: Astronaut)
•	Removes an astronaut from the collection.
find_by_name(name: str)
•	Returns an astronaut with that name if he/ she exists.
"""
from test.astronaut.astronaut import Astronaut


class AstronautRepository: # store all astronauts on space station
    def __init__(self):
        self.astronauts=[]

    def add(self,astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self,astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self,name: str):
        for each_astr in self.astronauts:
            if each_astr.name==name:
                return each_astr
        
