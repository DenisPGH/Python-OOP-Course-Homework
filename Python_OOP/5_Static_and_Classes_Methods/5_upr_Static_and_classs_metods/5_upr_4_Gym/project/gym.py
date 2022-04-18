""" There is a wrong value in the word file, it is wroten, 2, but have to return 1"""
from test.customer import Customer
from test.equipment import Equipment
from test.exercise_plan import ExercisePlan
from test.subscription import Subscription
from test.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers=[]
        self.trainers=[]
        self.equipment=[]
        self.plans=[]
        self.subscriptions=[]




    @staticmethod
    def return_object(id,lists):
        for each in lists:
            if each.id ==id:
                return each
    @staticmethod
    def prove_if_exist(object,lists):
        if object not in lists:
            return True
    def __make_id_and_store(self,object,lists):
        """ this help function make new id for the object and store the object ot corresponding list"""
        if len(lists) == 0:
            object.id = 1
            lists.append(object)
        elif len(lists) > 0:
            object.id = len(lists)+1
            object.__class__.id=object.id
            lists.append(object)

    def add_customer(self,customer: Customer):
        # - add the customer in the customer list if the customer is not already in it
        if Gym.prove_if_exist(customer,self.customers):
            self.__make_id_and_store(customer, self.customers)
            #self.customers.append(customer)

    # •	add_trainer(trainer: Trainer) - add the trainer to the trainers' list, if the trainer is not already in it
    def add_trainer(self,trainer: Trainer):
        # - add the customer in the customer list if the customer is not already in it
        if Gym.prove_if_exist(trainer,self.trainers):
            self.__make_id_and_store(trainer,self.trainers)

    def add_equipment(self,equipment: Equipment) :
        if Gym.prove_if_exist(equipment, self.equipment):
            self.__make_id_and_store(equipment, self.equipment)
            #self.equipment.append(equipment)

    def add_plan(self,plan: ExercisePlan): # - add the plan to the plans' list, if the plan is not already in it
        if Gym.prove_if_exist(plan, self.plans):
            self.__make_id_and_store(plan, self.plans)
            #self.plans.append(plan)

    def add_subscription(self, subscription: Subscription): # - add the subscription in the subscriptions list if the subscription is not already in it
        if Gym.prove_if_exist(subscription, self.subscriptions):
            self.__make_id_and_store(subscription, self.subscriptions)
            #self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id: int):
        # - get the subscription, the customer, the trainer, the equipment, and the plan.
        # Then return their string representations each on a new line.
        serached_subscription=Gym.return_object(subscription_id,self.subscriptions) # has
        id_of_customer=serached_subscription.customer_id

        searched_customer=Gym.return_object(id_of_customer,self.customers) # has

        searched_trainer=Gym.return_object(serached_subscription.trainer_id,self.trainers)
        searched_plan=Gym.return_object(searched_trainer.id,self.plans)
        serached_equipment=Gym.return_object(searched_plan.equipment_id,self.equipment)
        result=""
        result+=f"{serached_subscription}\n"
        result+=f"{searched_customer}\n"
        result+=f"{searched_trainer}\n"
        result+=f"{serached_equipment}\n"
        result+=f"{searched_plan}"
        return result



