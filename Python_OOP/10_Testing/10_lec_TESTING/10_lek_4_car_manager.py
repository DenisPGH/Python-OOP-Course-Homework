class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

"""
Your job now is to write unit project_ on the provided project_ and its functionality. 
You should project_ every part of the code inside the Car class:
•	You should project_ the constructor
•	You should project_ all the methods and validations inside the class
Constraints
•	Everything in the provided skeleton is working perfectly fine
•	You must not change anything in the project_ structure
•	Any part of validation should be tested
•	There is no limit on the project_ you can write but keep your attention on the main functionality
Note: You are not allowed to change the structure of the provided code
"""

import unittest
class CarTests(unittest.TestCase):
    make = "Deni"
    model = "A1"
    fuel_consumption = 2
    fuel_capacity = 10
    fuel_amount = 0
    # project_ constructor make, model, fuel_consumption, fuel_capacity):
    def test_input_values__if__store_correct(self):
        audi=Car("Deni","A1",2,10)
        self.assertEqual(self.make,audi.make)
        self.assertEqual(self.model,audi.model)
        self.assertEqual(self.fuel_consumption,audi.fuel_consumption)
        self.assertEqual(self.fuel_capacity,audi.fuel_capacity)
    # if make return right value
    def test_car_make_return_right_value(self):
        audi = Car("Deni", "A1", 2, 10)
        result=audi.make
        self.assertEqual(self.make, result)
    # project_ if wrong value raise exception by props make
    def test_setting_make__wrong_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.make=""
        self.assertEqual("Make cannot be null or empty!",str(context.exception))

    def test_setting_make__wrong_value_0__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.make=0
        self.assertEqual("Make cannot be null or empty!",str(context.exception))

    #project_ if wrong value raise exception by props make
    def test_setting_make__correct_value__return_new_value(self):
        audi = Car("Deni", "A1", 2, 10)
        audi.make = "Keti"
        self.assertEqual("Keti", audi.make)

    # now 4 project_ for model, same as make
    def test_car_model_return_right_value(self):
        audi = Car("Deni", "A1", 2, 10)
        result = audi.model
        self.assertEqual(self.model, result)

    # project_ if wrong value raise exception by props make
    def test_setting_model__wrong_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.model = ""
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_setting_model__wrong_value_0__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.model = 0
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    # project_ if wrong value raise exception by props make
    def test_setting_model__correct_value__return_new_value(self):
        audi = Car("Deni", "A1", 2, 10)
        audi.model = "Keti"
        self.assertEqual("Keti", audi.model)

    ### now 4 project_ for fuel_consupsino
    def test_car_fuel_consum_return_right_value(self):
        audi = Car("Deni", "A1", 2, 10)
        result = audi.fuel_consumption
        self.assertEqual(self.fuel_consumption, result)

    # project_ if wrong value raise exception by props make
    def test_setting_fuel_consumptio__wrong_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_setting_fuel_consum__wrong_value_0__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.fuel_consumption= 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    # project_ if wrong value raise exception by props make
    def test_setting_fuel_consump__correct_value__return_new_value(self):
        audi = Car("Deni", "A1", 2, 10)
        audi.fuel_consumption = 100
        self.assertEqual(100, audi.fuel_consumption)

    # 4 project_ for fuel_amount
    def test_car_fuel_amount_return_right_value(self):
        audi = Car("Deni", "A1", 2, 10)
        result = audi.fuel_amount
        self.assertEqual(self.fuel_amount, result)

    # project_ if wrong value raise exception by props make
    def test_setting_fuel_amount__wrong_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))


    # project_ if wrong value raise exception by props make
    def test_setting_fuel_amount__correct_value__return_new_value(self):
        audi = Car("Deni", "A1", 2, 10)
        audi.fuel_amount = 100
        self.assertEqual(100, audi.fuel_amount)

    """ 4 project_ for fuel capacity"""
    def test_car_fuel_capacity_return_right_value(self):
        audi = Car("Deni", "A1", 2, 10)
        result = audi.fuel_capacity
        self.assertEqual(self.fuel_capacity, result)

    # project_ if wrong value raise exception by props make
    def test_setting_fuel_capacity__wrong_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_setting_fuel_capacity__wrong_value_0__return_exc(self):
        audi = Car("Deni", "A1", 2, 10)
        with self.assertRaises(Exception) as context:
            audi.fuel_capacity= 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    # project_ if wrong value raise exception by props make
    def test_setting_fuel_capacity__correct_value__return_new_value(self):
        audi = Car("Deni", "A1", 2, 10)
        audi.fuel_capacity = 100
        self.assertEqual(100, audi.fuel_capacity)

    """ project_ 4 for refuel"""
    def test_car_refuel_seter_return_right_value(self):
        audi = Car("Deni", "A1", 2, 30)
        audi.refuel(10)
        self.assertEqual(10, audi.fuel_amount)

    def test_setting_refuel__negtive_value__return_exc(self):
        audi = Car("Deni", "A1", 2, 30)
        with self.assertRaises(Exception) as context:
            audi.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_setting_refuel__wrong_value_0__return_exc(self):
        audi = Car("Deni", "A1", 2, 30)
        with self.assertRaises(Exception) as context:
            audi.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    # project_ if wrong value raise exception by props make
    def test_setting_refuel__more_fuel_than_capacity__return_value_of_capcity(self):
        audi = Car("Deni", "A1", 2, 30)
        audi.refuel(40)
        self.assertEqual(30, audi.fuel_amount)
    """    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed"""
    def test_drive_if_needed_is_enought_for_distance__reduce_amount(self):
        audi = Car("Deni", "A1", 2, 30)
        audi.refuel(10)
        audi.drive(10)
        needed = 0.2
        self.assertEqual(9.8,audi.fuel_amount)

    def test_drive_if_needed_is_more_for_distance__raise_exect(self):
        audi = Car("Deni", "A1", 5, 30)
        audi.refuel(1)
        with self.assertRaises(Exception) as context:
            audi.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))




if __name__=="__main__":
    unittest.main()

