from test.car import Car

class FamilyCar(Car):
    #DEFAULT_FUEL_CONSUMPTION=3
    def __init__(self,fuel, horse_power):
        super().__init__(fuel,horse_power)
        #self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION

    def drive(self,kilometers):
        if self.fuel>=(kilometers*self.fuel_consumption):
            self.fuel-=(kilometers*self.fuel_consumption)