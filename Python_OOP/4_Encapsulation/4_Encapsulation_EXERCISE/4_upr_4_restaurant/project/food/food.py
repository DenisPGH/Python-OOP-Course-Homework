

"""Beverage and Food classes are products:
•	The Beverage class should have an additional
 private attribute – milliliters: float and its subsequent getter

•	The Food class should have an additional 
private attribute – grams: float and its subsequent getter
"""
from test.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        self.__grams = value

