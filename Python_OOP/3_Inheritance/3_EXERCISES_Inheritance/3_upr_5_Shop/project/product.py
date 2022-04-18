"""In the product.py file, the class Product should be implemented.
 It is a base class for any type of food and drink.
The class should receive name: str, and quantity: int upon initialization.
It should also have 3 additional methods:
•	decrease(quantity: int) - decreases the quantity of the product only if there is enough
•	increase(quantity: int) - increases the quantity of the product
•	__repr__() - override the method, so it returns the name of the product
"""
class Product:  # base class for all food and drink
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self,quantity):
        if self.quantity-quantity>=0:
            self.quantity-=quantity

    def increase(self,quantity): #int) - increases the quantity of the product
        self.quantity+=quantity

    def __repr__(self):
        return self.name