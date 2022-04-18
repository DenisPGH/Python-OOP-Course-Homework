
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


"""
•	#  Test if the worker is initialized with the correct name, salary, and energy
•	#  Test if the worker's energy is incremented after the rest method is called
•	# Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	#Test if the worker's money is increased by his salary correctly after the work method is called
•	# Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values
"""
import unittest


class WorkerTests(unittest.TestCase):
    valid_name="Deni"
    valid_salary= 1000
    valid_energy=10
    money=0


    def test_get_name_salary_energy__valid_data__return_valid(self):
        deni=Worker(self.valid_name,self.valid_salary,self.valid_energy)
        self.assertEqual(self.valid_name,deni.name)
        self.assertEqual(self.valid_salary,deni.salary)
        self.assertEqual(self.valid_energy,deni.energy)

    def test_if_energy_incrementet_after_rest__return_more(self):
        deni = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        deni.rest()
        self.assertEqual(self.valid_energy+1,deni.energy)

    def test_try_work__with_negative_energy__return_exception(self):
        deni = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception) as context:
            deni.work()

        self.assertEqual('Not enough energy.',str(context.exception))


    def test_if_money_increased__after_method_work__return(self):
        deni = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        deni.work()

        self.assertEqual(self.money+self.valid_salary,deni.money)


    def test_if_energy_decreased_after_work_method_called(self):
        deni = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        deni.work()
        self.assertEqual(self.valid_energy-1, deni.energy)


    def test_if_get_info_equal_to_right_string(self):
        deni = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        result=deni.get_info()
        correct=f'{self.valid_name} has saved {self.money} money.'

        self.assertEqual(correct, result)


if __name__ == "__main__":
    unittest.main()















