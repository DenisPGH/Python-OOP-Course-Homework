"""In the file drink.py, the class Drink should be implemented.
 The class should inherit from the Product class. An instance of the
  Drink class will have a name and a quantity of 10."""
from test.product import Product
class Drink(Product):
    def __init__(self,name):
        super().__init__(name,10) # give direct default value to quantity