"""Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter.
Create classes Circle (receives radius upon initialization)
and Rectangle (receives height and width upon initialization)
that implement those methods (returning the result).
 The fields of Circle and Rectangle should be private==abstraction."""
import math
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,raduis):
        self.raduis = raduis

    def calculate_area(self):
        return math.pi *self.raduis*self.raduis

    def calculate_perimeter(self):
        return math.pi * 2 *self.raduis

class  Rectangle(Shape): # (receives height and width upon initialization)
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return  self.height * self.width

    def calculate_perimeter(self):
        return  (2*self.width)+(2*self.height)



# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
#
#
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())


