
from test.customer import Customer
from test.dvd import DVD


class MovieWorld:
    def __init__(self,name):
        self.name = name
        self.customers=[] # store all customers
        self.dvds=[] # store all dvd
    # dvd_capacity() - returns 15 - the DVD capacity of a movie world
    # •	customer_capacity() - returns 10 - the customer capacity of a movie world
    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self,customer: Customer): # - add the customer if capacity not exceeded
        if len(self.customers)<MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self,dvd: DVD): # - add the DVD if capacity not exceeded
        if len(self.dvds)<MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __return_instance_from_id(self,instance_id,lists):
        for each_object in lists:
            if each_object.id==instance_id:
                return each_object

        return None






     # - if the DVD is in the customer,
# he/she should return it and the method should return the
# message "{customer_name} has successfully returned {dvd_name}".
# Otherwise, return "{customer_name} does not have that DVD"
    def return_dvd(self,customer_id, dvd_id) :
        dvd_object = self.__return_instance_from_id(dvd_id, self.dvds)
        curent_name=""
        for each_customer in self.customers:
            if each_customer.id==customer_id:
                curent_name=each_customer.name
                for each_dvd in each_customer.rented_dvds:
                    if each_dvd.id==dvd_id:
                        each_customer.rented_dvds.remove(each_dvd)
                        # here have to make dvd free again !!!!!
                        dvd_object.is_rented=False
                        return  f"{each_customer.name} has successfully returned {each_dvd.name}"

        return f"{curent_name} does not have that DVD"

    #return the string representation of each customer and each DVD on separate lines
    def __repr__(self):
        result=""
        for each_customer in self.customers:
            result+=f"{each_customer}\n"

        for each_dvd in self.dvds:
            result += f"{each_dvd}\n"

        return result

    #
    def rent_dvd(self, customer_id: int, dvd_id: int):
        person_object=self.__return_instance_from_id(customer_id,self.customers)
        dvd_object=self.__return_instance_from_id(dvd_id,self.dvds)
        if dvd_object in person_object.rented_dvds: # if he has already
            return f"{person_object.name} has already rented {dvd_object.name}"
        for each_person in self.customers:
            for each_dvd in each_person.rented_dvds:
                if dvd_id==each_dvd.id and each_person.name !=person_object.name:
                    return "DVD is already rented"

        if person_object.age<= dvd_object.age_restriction:
            return f"{person_object.name} should be at least {dvd_object.age_restriction} to rent this movie"

        person_object.rented_dvds.append(dvd_object)
        dvd_object.is_rented=True
        return  f"{person_object.name} has successfully rented {dvd_object.name}"




"""
•	
o	
o	If the customer is not allowed to rent the DVD, return "{customer_name}
 should be at least {dvd_age_restriction} to rent this movie"
o	Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs).
 Return "{customer_name} has successfully rented {dvd_name}"
"""

