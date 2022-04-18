"""In the file geodesist.py, the class Geodesist should be implemented. The geodesist is a type of astronaut.
Each geodesist has 50 initial units of oxygen."""
from project_.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)