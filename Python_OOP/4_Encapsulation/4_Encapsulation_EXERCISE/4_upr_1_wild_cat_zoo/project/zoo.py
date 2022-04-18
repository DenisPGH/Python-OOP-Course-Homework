"""The Zoo class should receive 4 attributes upon initialization:
•	Public attribute name: string
•	Private attribute budget: int
•	Private attribute animal_capacity: int
•	Private attribute workers_capacity: int
It should also have 2 instance attributes:
•	Public attribute animals: list - (empty upon initialization)
•	Public attribute workers: list - (empty upon initialization)
"""
###
class Zoo:
    def __init__(self,name,budget,animal_capacity,workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals=[]
        self.workers=[]

    # •	add_animal(animal, price)
    # o	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah)
    # to the animals' list, reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)}
    # added to the zoo"
    # o	If you have the capacity, but no budget, return "Not enough budget"
    # o	In any other case, you do not have space, and you should return "Not enough space for animal"
    def add_animal(self,animal, price):
        if self.__animal_capacity>0 and self.__budget-price>=0:
            self.__budget-=price # reduce the price
            self.__animal_capacity-=1 # reduce capacity of animals
            self.animals.append(animal) # add obect to the list  Cheetah("Cheeto", "Male", 2),
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__animal_capacity>0 and self.__budget-price<0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    #
    #•	hire_worker(worker)
    #o	If you have not exceeded the capacity of workers in the zoo for the worker
    # (instance of Keeper/Caretaker/Vet), add him to the workers and
    # return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
    #o	Otherwise, return "Not enough space for worker"
    def hire_worker(self,worker):
        if self.__workers_capacity<=0:
            return "Not enough space for worker"
        self.workers.append(worker) #add to the list worker
        self.__workers_capacity-=1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    #
    #•	fire_worker(worker_name)
# o	If there is a worker with that name in the workers' list, remove him and
# return "{worker_name} fired successfully"
# o	Otherwise, return "There is no {worker_name} in the zoo"
    def fire_worker(self,worker_name):
        for each_worker in self.workers:
            if each_worker.name==worker_name:
                self.workers.remove(each_worker)
                self.__workers_capacity += 1

                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    #
    #•	pay_workers()
# o	If you have enough budget to pay the workers (sum their salaries) pay them and
# return "You payed your workers. They are happy. Budget left: {left_budget}"
# o	Otherwise, return "You have no budget to pay your workers. They are unhappy"
    def pay_workers(self):
        sum_salaries=0
        for each_worker in self.workers:
            sum_salaries+=each_worker.salary
        if sum_salaries>self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    #
    #•	tend_animals()
#o	If you have enough budget to take care of the animals, reduce the budget and
# return "You tended all the animals. They are happy. Budget left: {left_budget}"
#o	Otherwise, return "You have no budget to tend the animals. They are unhappy."
    def tend_animals(self):
        sum_care=0
        for each_animal in self.animals:
            sum_care+=each_animal.money_for_care
        if sum_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget }"
    #•	profit(amount)
#o	Increase the budget with the given amount of profit
    def profit(self,amount):
        self.__budget+=amount

    """•	animals_status()
o	Returns the following string (Hint: use the __repr__ methods of the animals to print 
them on the console):
"You have {total_animals_count} animals
----- {amount_of_lions} Lions:
{lion1}
…
{lionN}
----- {amount_of_tigers} Tigers:
{tiger1}
…
{tigerN}
----- {amount_of_cheetahs} Cheetahs:
{cheetah1}
…
{cheetahN}"
"""

    def animals_status(self):
        result=f"You have {len(self.animals)} animals\n"
        dict_animals={}
        for each in self.animals:
            if each.__class__.__name__ not in dict_animals:
                dict_animals[each.__class__.__name__]=[]
            dict_animals[each.__class__.__name__].append(each)
        result += f"----- {len(dict_animals['Lion'])} Lions:\n"
        for each_animal in dict_animals['Lion']:
            result+=f"{each_animal}\n"
        result += f"----- {len(dict_animals['Tiger'])} Tigers:\n"
        for each_animal in dict_animals['Tiger']:
            result += f"{each_animal}\n"
        result += f"----- {len(dict_animals['Cheetah'])} Cheetahs:\n"
        for each_animal in dict_animals['Cheetah']:
            result += f"{each_animal}\n"


        return result.rstrip('\n') # have to print by class

    #•	workers_status()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        dict_workers = {}
        for each in self.workers:
            if each.__class__.__name__ not in dict_workers:
                dict_workers[each.__class__.__name__] = []
            dict_workers[each.__class__.__name__].append(each)
        result += f"----- {len(dict_workers['Keeper'])} Keepers:\n"
        for each_worker in dict_workers['Keeper']:
            result += f"{each_worker}\n"
        result += f"----- {len(dict_workers['Caretaker'])} Caretakers:\n"
        for each_worker in dict_workers['Caretaker']:
            result += f"{each_worker}\n"
        result += f"----- {len(dict_workers['Vet'])} Vets:\n"
        for each_worker in dict_workers['Vet']:
            result += f"{each_worker}\n"

        return result.rstrip('\n') # have to print by class


"""	Returns the following string (Hint: use the __repr__ methods of the workers to print
 them on the console):
"You have {total_workers_count} workers
----- {amount_of_keepers} Keepers:
{keeper1}
…
{keeperN}
----- {amount_of_caretakers} Caretakers:
{caretaker1}
…
{caretakerN}
----- {amount_of_vetes} Vets:
{vet1}
…
{vetN}"

"""









