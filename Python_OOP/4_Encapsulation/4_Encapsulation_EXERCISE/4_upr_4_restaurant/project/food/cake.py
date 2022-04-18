"""Cake is a dessert. Also, it must have the following class attributes
which should apply to all cakes made:
•	GRAMS = 250 (constant)
•	CALORIES = 1000 (constant)
•	PRICE = 5 (constant)
"""
from test.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self,name):
        super().__init__(name,Cake.PRICE,Cake.GRAMS,Cake.CALORIES)