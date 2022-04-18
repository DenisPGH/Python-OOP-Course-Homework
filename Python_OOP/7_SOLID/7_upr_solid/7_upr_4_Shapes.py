"""You are provided with code containing class Rectangle and class AreaCalculator.
 Refactor the code using the Open/Closed Principle so that the code is open for extension
  (adding more shapes) but closed for modification."""
from abc import ABC,abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Figure):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height


    def area(self):
        return self.width*self.height


class Triangle(Figure):

    def __init__(self, side, height):
        super().__init__()
        self.side = side
        self.height = height

    def area(self):
        return (self.side * self.height)/2

class Squear(Figure):

    def __init__(self, side):
        super().__init__()
        self.side = side


    def area(self):
        return (self.side * self.side)


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total




shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

print(" ==== AFTER =====")

shapes = [Rectangle(1, 6), Triangle(2, 3),Squear(4)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

