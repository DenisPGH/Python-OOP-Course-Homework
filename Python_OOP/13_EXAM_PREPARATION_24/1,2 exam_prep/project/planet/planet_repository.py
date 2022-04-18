"""In the planet_repository.py file, the class PlanetRepository should be implemented.
 It is a repository for planets that await to be explored.
Structure
The class should have the following attributes:
•	planets: an empty list of planets
Methods
__init__()
The __init__ method should have an empty list of planets.
add(planet: Planet)
•	Adds a planet for exploration.
remove(planet: Planet)
•	Removes a planet from the collection.
find_by_name(name: str)
•	Returns a planet with that name if it exists.
"""
from test.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets=[]

    def add(self,planet: Planet):
        self.planets.append(planet)

    def remove(self,planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self,name: str):
        for each_planet in self.planets:
            if each_planet.name==name:
                return each_planet


