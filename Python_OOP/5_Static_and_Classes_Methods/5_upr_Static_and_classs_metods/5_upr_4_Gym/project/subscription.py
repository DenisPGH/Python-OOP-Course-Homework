"""
Implement the __repr__ method so it returns the info about the subscription in the following
format: "Subscription <{id}> on {date}"
Create a static method called get_next_id which returns the id that will be given to the next subscription
"""
class Subscription:
    id=1
    def __init__(self,date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date=date
        self.customer_id=customer_id
        self.trainer_id=trainer_id
        self.exercise_id=exercise_id

    @staticmethod
    def get_next_id():
        #Subscription.id += 1
        return Subscription.id


    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"


