"""Starter, MainDish, and Dessert are food:
•	The Dessert class should have an
additional private attribute - calories - float and its subsequent getter
"""
from test.food.food import Food


class Dessert(Food):
    def __init__(self,name,price,grams,calories):
        super().__init__(name,price,grams)
        self.calories=calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories=value
