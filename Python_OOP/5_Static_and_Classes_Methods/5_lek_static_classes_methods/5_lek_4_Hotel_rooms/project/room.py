"""   The class should have 2 additional methods:
•	take_room(people) - if the room is not taken, and there is enough space, the guests take the room.
 Otherwise, the method should return "Room number {number} cannot be taken"
•	free_room() - if the room is taken, free it. Otherwise, return "Room number {number} is not taken"
"""
class Room:
    def __init__(self,number,capacity):
        self.number = number
        self.capacity = capacity
        self.guests=0
        self.is_taken=False

    def take_room(self,people):
        if self.is_taken==True or people>self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken=True
        self.capacity-=people
        self.guests+=people

    def free_room(self):
        if self.is_taken==False:
            return f"Room number {self.number} is not taken"
        self.is_taken=False
        self.guests=0


