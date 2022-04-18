"""In the file meteorologist.py, the class Meteorologist should be implemented.
The meteorologist is a type of astronaut. Each meteorologist has 90 initial units of oxygen,
and each time they take a breath, their oxygen is decreased by 15 units."""
from project_.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    DEFAULT_BREATH_VALUE = 15
    def __init__(self, name):
        super().__init__(name, 90)

    # def breathe(self):
    #     self.oxygen-=self.DEFAULT_BREATH_VALUE
