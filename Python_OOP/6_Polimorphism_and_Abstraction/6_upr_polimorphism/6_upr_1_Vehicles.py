"""Create an abstract class called Vehicle that should have abstract methods drive and refuel. """
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self,distance):
        pass

    @abstractmethod
    def refuel(self,fuel):
        pass

"""Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and
 simulates driving and refueling them. """

# and their fuel consumption per km when driving is increased by 0.9 liters for the car
# and 1.6 liters for the truck.
class Car(Vehicle):
    def __init__(self,fuel_quantity,fuel_consumption ): # in liters per km upon initialization
        self.fuel_quantity = fuel_quantity # how much literes has
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        if self.fuel_quantity-(distance*(self.fuel_consumption+0.9))<0:
            return
        self.fuel_quantity-= (distance*(self.fuel_consumption+0.9))# reduce the value


    def refuel(self,fuel):
        self.fuel_quantity+=fuel



class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity-(distance*(self.fuel_consumption+1.6))<0:
            return
        self.fuel_quantity -= (distance * (self.fuel_consumption + 1.6))  # reduce the value

    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95



# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# car.drive(1)
# print(car.fuel_quantity)


# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
