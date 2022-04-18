import unittest

from test.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    DEFAULT_FUEL_CONSUMPTION= 1.25
    fuel_consumption= 1.25
    fuel= 1
    capacity= 1
    horse_power= 10
    def test_if_gived_values_are_corect_by_incialisation(self):
        moto=Vehicle(self.fuel,self.horse_power)
        self.assertEqual(self.fuel,moto.fuel)
        self.assertEqual(self.capacity,moto.capacity)
        self.assertEqual(self.fuel_consumption,moto.fuel_consumption)
        self.assertEqual(self.horse_power,moto.horse_power)

    """    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel < fuel_needed:
            raise Exception("Not enough fuel")
        self.fuel -= fuel_needed"""
    def test_drive__giving_long_distance__return_exception(self):
        moto = Vehicle(self.fuel, self.horse_power)
        with self.assertRaises(Exception) as context:
            moto.drive(200)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__giving_short_distance__reduce_fuel(self):
        moto = Vehicle(5, self.horse_power)
        moto.drive(2)
        self.assertEqual(2.5, moto.fuel)
    """    def refuel(self, fuel):
        if self.fuel + fuel > self.capacity:
            raise Exception("Too much fuel")
        self.fuel += fuel"""
    def test_refuel__giving_to_much__return_exception(self):
        moto = Vehicle(self.fuel, self.horse_power)
        with self.assertRaises(Exception) as context:
            moto.refuel(200)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_drive__giving__correct_fuel__increace_fuel(self):
        moto = Vehicle(5, self.horse_power)
        moto.drive(3)
        moto.refuel(2)
        self.assertEqual(3.25, moto.fuel)
    def test_if_str_method_return_correct_string(self):
        moto = Vehicle(5, self.horse_power)
        resutlt=str(moto)
        haveto=f"The vehicle has {moto.horse_power} " \
               f"horse power with {moto.fuel} fuel left and {moto.fuel_consumption} fuel consumption"
        self.assertEqual(haveto, resutlt)







if __name__=="__main__":
    unittest.main()

