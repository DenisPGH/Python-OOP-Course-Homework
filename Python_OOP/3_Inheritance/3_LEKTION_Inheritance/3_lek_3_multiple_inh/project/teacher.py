# •	Teacher with a single method teach() that returns: "teaching...".
from test.person import Person
from test.employee import Employee
class Teacher(Person,Employee):
    def teach(self):
        return "teaching..."