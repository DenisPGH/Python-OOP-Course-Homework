""": Each plan should also have an id (autoincremented, starting from 1).
To do the incrementation, you should create a class attribute id equal to 1,
which will keep the value of the id for the next plan's id. Create the following methods:
•	from_hours(trainer_id:int, equipment_id:int, hours:int) -
 creates new instance using the provided information
•	get_next_id() - static method that returns the id that will be given to the next plan
•	__repr__() - returns the information about the plan in the following format:
 "Plan <{id}> with duration {duration} minutes"
"""
class ExercisePlan:
    id=1
    def __init__(self,trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration # (in minutes)

    @staticmethod
    def get_next_id():
        #ExercisePlan.id += 1
        return ExercisePlan.id
    @classmethod
    def from_hours(cls,trainer_id:int, equipment_id:int, hours:int):
        mins=hours*60
        return cls(trainer_id,equipment_id,mins)


    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


