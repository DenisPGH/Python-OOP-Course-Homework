"""HotBeverage and ColdBeverage are beverages."""
from test.beverage.beverage import Beverage


class HotBeverage(Beverage):
    def __init__(self,name,price,milliliters):
        super().__init__(name,price,milliliters)