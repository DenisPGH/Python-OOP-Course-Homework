from test.vehicle import Vehicle
"""Each class should have the following methods:
•	drive(kilometers) - reduces the fuel based on the traveled kilometers
 and fuel consumption (km * fuel consumption). Keep in mind that you can start driving the 10_upr_2_vehicle
 only if you have enough fuel to finish the driving.
 """

class Motorcycle(Vehicle):
    def __init__(self,fuel, horse_power):
        super().__init__(fuel,horse_power)

    def drive(self,kilometers):
        if self.fuel>=(kilometers*self.fuel_consumption):
            self.fuel-=(kilometers*self.fuel_consumption)