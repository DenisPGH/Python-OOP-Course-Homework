"""You are provided with a code containing a class Prisoner and a class Person.
 A prisoner is obviously a person, but since a prisoner is not free to move an arbitrary distance,
  the Person class can be named FreePerson, then the idea that a Prisoner inherits FreePerson is wrong.
   Rewrite the code and apply the LSP (Liskov Substitution Principle).

   SOLUTION====
   -make same structure as in Person, and add ==> if Prisioner.is_free==True,then add distance to coordiante
"""

import copy
class Person:
    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

class FreePerson(Person):
    pass




class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(self.PRISON_LOCATION)
        self.is_free = False

    def walk_north(self, dist):
        if self.is_free== True:
            self.position[1] += dist

    def walk_east(self, dist):
        if self.is_free == True:
            self.position[0] += dist




"""TEST START HERE !!!"""
prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")


# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")
#
# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")
"""BEFORE
 The prisoner trying to walk to north by 10 and east by -3.
The location of the prison: [3, 3]
The current position of the prisoner: [0, 13]
"""
a=0

"""
The prisoner trying to walk to north by 10 and east by -3.
The location of the prison: (3, 3)
The current position of the prisoner: (3, 3)
"""