"""In the food.py file, the Food class should be implemented.
 The class should inherit from the Product class. An instance of
 the Food class will have a name and a quantity of 15."""
from test.product import Product

class Food(Product):
    def __init__(self,name):
        super().__init__(name,15) # give direct default value to quantity