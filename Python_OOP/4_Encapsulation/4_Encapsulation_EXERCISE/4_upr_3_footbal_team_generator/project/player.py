"""
Create a class called Player. Upon initialization, it should receive:
•	Private attribute name: string
•	Private attribute sprint: int
•	Private attribute dribble: int
•	Private attribute passing: int
•	Private attribute shooting: int
"""
class Player:
    def __init__(self,name,sprint,dribble,passing,shooting):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name=value

    def __str__(self):
        result=f"Player: {self.__name}\n"
        result+=f"Sprint: {self.__sprint}\n"
        result+=f"Dribble: {self.__dribble}\n"
        result+=f"Passing: {self.__passing}\n"
        result+=f"Shooting: {self.__shooting}"
        return result






