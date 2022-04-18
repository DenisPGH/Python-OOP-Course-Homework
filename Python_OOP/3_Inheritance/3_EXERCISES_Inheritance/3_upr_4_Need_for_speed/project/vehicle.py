""" Create a base class Vehicle. It should contain the following attributes:
•	DEFAULT_FUEL_CONSUMPTION: float (constant)
•	fuel_consumption: float - represents the fuel consumption per kilometer
•	fuel: float - represents the quantity of fuel in a specific 10_upr_2_vehicle
•	horse_power: int
Upon initialization, the class should receive fuel and horse_power.
The DEFAULT_FUEL_CONSUMPTION value should be set to the fuel_consumption value.
Each class should have the following methods:
•	drive(kilometers) - reduces the fuel based on the traveled kilometers
 and fuel consumption (km * fuel consumption). Keep in mind that you can start driving the 10_upr_2_vehicle
 only if you have enough fuel to finish the driving.
 """

# The default fuel consumption for the different vehicles is:
# •	Vehicle is 1.25
# •	SportCar is 10
# •	RaceMotorcycle is 8
# •	Car is 3


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION =1.25   # Vehicle is 1.25, SportCar is 10, RaceMotorcycle is 8, Car is 3
    def __init__(self,fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        #self.fuel_consumption=Vehicle.DEFAULT_FUEL_CONSUMPTION# - represents the fuel consumption per kilometer
        self.fuel_consumption=self.DEFAULT_FUEL_CONSUMPTION# - represents the fuel consumption per kilometer
        # with self.DEFAULT_FUEL get each class better, than Vehicle.DEFAULT_FUEL



    def drive(self,kilometers):
        if self.fuel>=(kilometers*self.fuel_consumption):
            self.fuel-=(kilometers*self.fuel_consumption)



