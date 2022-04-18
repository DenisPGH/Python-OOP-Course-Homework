"""
•	from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
•	add_room(room: Room) - adds the room to the list of rooms
•	take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
•	free_room(room_number) - finds the room with that number and tries to free it
•	status() - returns information about the hotel in the following format:
"Hotel {name} has {guests} total guests
Free rooms: {numbers of all free rooms separated by comma and space}
Taken rooms: {numbers of all taken rooms separated by comma and space}"
Examples
"""
from test.room import Room


class Hotel:
    def __init__(self,name):
        self.name = name
        self.rooms=[] # store all numbers of rooms
        self.guests=0 # count guests
    # from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
    @classmethod
    def from_stars(cls,stars_count):
        return cls(f"{stars_count} stars Hotel")

    # add_room(room: Room) - adds the room to the list of rooms
    def add_room(self,room: Room):
        self.rooms.append(room)

    #take_room(room_number, people) - finds the room with that number and tries to accommodate the
    # guests in the room
    def take_room(self,room_number, people):
        for each_room in self.rooms:
            if each_room.number==room_number:
                if people<=each_room.capacity:
                    self.guests+=people
                each_room.take_room(people)



    def free_room(self,room_number): # - finds the room with that number and tries to free it
        for each_room in self.rooms:
            if each_room.number==room_number:
                self.guests -= each_room.guests
                each_room.free_room()


    def status(self): #- returns information about the hotel in the following format:
        result=f"Hotel {self.name} has {self.guests} total guests\n"
        result+=F"Free rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken==False])}\n"
        result+=f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken==True])}"

        return result






