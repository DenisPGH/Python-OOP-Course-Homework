"""Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str).
 Implement the needed magic methods so that:
•	Each person could be represented by their names, separated by a single space.
•	When you concatenate two people,
you should return a new instance of a person who will take the first name from
the first person and the surname from the second person.
"""

class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    @classmethod
    def new_names(cls,name,surname):
        return cls(name,surname)

    def __add__(self, other):
        return self.new_names(self.name,other.surname)



    def __repr__(self):
        return f"{self.name} {self.surname}"


d=Person("Deni","Petrov")
k=Person("Keti","Gesheva")

#print(d+k)

"""Create another class called Group. Upon initialization, it should receive a name (str) and people
 (list of Person instances). Implement the needed magic methods so that:"""
class Group:
    def __init__(self,name,*args):
        self.name = name
        self.people=list(*args)




    #•	When you access the length of a group instance, you should receive the total number of people in the group.
    def __len__(self):
        return len(self.people)

    #•	When you concatenate two groups, you should return a new instance of a group which
    # will have a name -string in the format "{first_name} {second_name}" and all the people
    # in the two groups will participate in the new one too.
    @classmethod
    def new_name_group(cls,name,surname,list_1,list_2):
        new_=f"{name} {surname}"
        new_members=[]
        new_members.extend(list_1)
        new_members.extend(list_2)
        return cls(new_,new_members)



    def __add__(self, other):
        return self.new_name_group(self.name,other.name,self.people,other.people)

    # •	Each group should be represented in the format
    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(x) for x in self.people])}"

    # •	You could iterate over a group, and each person (element of the group)
    # should be represented in the format
    def __getitem__(self, item):

        stri=f"Person {item}: {self.people[item]}"
        return stri










# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
# 
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
# print(third_group)
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
# #
# for person in third_group:
#     print(person)
#
#
#
#
#
