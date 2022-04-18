"""In the file biologist.py, the class Biologist should be implemented.
The biologist is a type of astronaut. Each biologist has 70 initial units of oxygen,
and each time they take a breath, their oxygen is decreased by 5 units."""
from project_.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    DEFAULT_BREATH_VALUE = 5
    def __init__(self, name):
        super().__init__(name, 70)

    # def breathe(self):
    #     self.oxygen-=self.DEFAULT_BREATH_VALUE