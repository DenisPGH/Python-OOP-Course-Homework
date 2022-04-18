"""In the space_station.py file, the class SpaceStation should be implemented.
Structure
The class should have the following attributes:
•	planet_repository: a new repository created for each space station
•	astronaut_repository: a new repository created for each space station
"""
from collections import deque

from project_.astronaut.astronaut_repository import AstronautRepository
from project_.astronaut.biologist import Biologist
from project_.astronaut.geodesist import Geodesist
from project_.astronaut.meteorologist import Meteorologist
from project_.planet.planet import Planet
from project_.planet.planet_repository import PlanetRepository



class SpaceStation:
    VALID_TYPES_ASTRONAUTS=["Biologist", "Geodesist", "Meteorologist"]
    def __init__(self):
        self.planet_repository=PlanetRepository()
        self.astronaut_repository=AstronautRepository()
        self.__succesfull_misions=0
        self.__unsuccesfull_misions=0
    """add_astronaut(astronaut_type: str, name: str) 
•	Creates an astronaut with the given name of the given type, adds them to the repository 
and returns the following message: "Successfully added {astronaut_type}: {astronaut_name}."
•	If an astronaut with that name is already in the repository 
returns: "{astronaut_name} is already added."
•	The valid astronaut types are "Biologist", "Geodesist" and "Meteorologist".
 If the astronaut type is invalid, raise an Exception with the message: "Astronaut type is not valid!"
"""
    def _check_object_by_name(self,name,list_):
        """ check for the object in the list"""
        if list_:
            for each in list_:
                if each.name==name:
                    return True
            else:
                return False
    def __create_astronaut(self,type_,name):
        if type_ == Biologist.__name__:
            return Biologist(name)
        if type_ == Geodesist.__name__:
            return Geodesist(name)
        if type_ == Meteorologist.__name__:
            return Meteorologist(name)

    def add_astronaut(self,astronaut_type:str, name: str):
        if astronaut_type not in self.VALID_TYPES_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")
        if self._check_object_by_name(name,self.astronaut_repository.astronauts):
            return f"{name} is already added."
        person_to_add=self.__create_astronaut(astronaut_type,name)
        self.astronaut_repository.astronauts.append(person_to_add)
        return f"Successfully added {astronaut_type}: {name}."




    #add_planet(name: str, items: str)
#•	Creates a planet with the provided name and items (single string with words, separated by ", "),
    # adds it to the repository, and returns the following message: "Successfully added Planet: {planet_name}."
#•	If a planet with that name is already in the repository returns: "{planet_name} is already added."
    def add_planet(self,name: str, items: str):
        if self._check_object_by_name(name,self.planet_repository.planets):
            return f"{name} is already added."
        planet_to_add=Planet(name)
        planet_to_add.items= items.split(', ')
        self.planet_repository.planets.append(planet_to_add)

        return  f"Successfully added Planet: {name}."


    """retire_astronaut(name: str)
•	Retires the astronaut from the space station by removing them from the repository and
 returns the following message: "Astronaut {astronaut_name} was retired!"
•	 If an astronaut with that name doesn't exist, raise Exception with the
 following message: "Astronaut {astronaut_name} doesn't exist!"
"""
    def retire_astronaut(self,name: str):
        if not self._check_object_by_name(name,self.astronaut_repository.astronauts):
            raise Exception(f"Astronaut {name} doesn't exist!")
        for each_astr in self.astronaut_repository.astronauts:
            if each_astr.name==name:
                self.astronaut_repository.astronauts.remove(each_astr)
                return f"Astronaut {name} was retired!"

    # recharge_oxygen()
    # •	The method increases the oxygen of each astronaut by 10 units. There is no capacity limit.
    def recharge_oxygen(self):
        for each_astr in self.astronaut_repository.astronauts:
            each_astr.oxygen+=10

    # send_on_mission(planet_name: str)
    """•	You should start by choosing the astronauts that are most suitable for the mission:
o	You should pick up to 5 astronauts with the highest amount of oxygen among the ones with 
oxygen above 30 units.
o	If you don't have any suitable astronauts, raise an Exception with the following message:
 "You need at least one astronaut to explore the planet!"
"""
    def return_object_by_name(self,name,list_):
        for each in list_:
            if each.name==name:
                return each
    def send_on_mission(self,planet_name: str):
        if not self._check_object_by_name(planet_name,self.planet_repository.planets):
            raise Exception("Invalid planet name!")
        suitable_astronauts={}
        final_astr_list=[]
        astronauts_which_got=0
        for each_astr in self.astronaut_repository.astronauts:
            if each_astr.oxygen>30:
                suitable_astronauts[each_astr.name]=each_astr.oxygen # here add all astr above 30 units
        counter=0
        if len(suitable_astronauts) >0:
            for ast_name,astr_oxy in sorted(suitable_astronauts.items(), key= lambda x: -x[1]):
                if counter>5:
                    break
                # here add in sorted descending order first 5 astr or less above 30 in a list with objects
                final_astr_list.append(self.return_object_by_name(ast_name,self.astronaut_repository.astronauts))
                counter+=1

        if len(final_astr_list)==0:
            raise Exception("You need at least one astronaut to explore the planet!")
        """•	The astronauts start going out in open space one by one, sorted in descending order
         by the amount of oxygen they have:
o	An astronaut lands on a planet and starts collecting its items one by one starting from the 
last one in the collection. Each time he/she finds an item he/she takes a breath.
o	If an astronaut runs out of oxygen, he/ she should return to the space station, 
and the next astronaut starts exploring
"""
        deq_list=deque(final_astr_list.copy())
        list_going_out=final_astr_list.copy()
        target_planet = self.return_object_by_name(planet_name, self.planet_repository.planets)
        for current_astronaut in list_going_out:

            if len(target_planet.items)==0:
                self.__succesfull_misions+=1
                return f"Planet: {planet_name} was explored. {astronauts_which_got} astronauts participated in collecting items."
            astronauts_which_got += 1
            while current_astronaut.oxygen>0:
                if target_planet.items:
                    last_item_of_the_planet=target_planet.items.pop() # remove last from the item on the planet
                    current_astronaut.backpack.append(last_item_of_the_planet) # the current ast got the item
                    current_astronaut.breathe()
                else:
                    self.__succesfull_misions += 1
                    return f"Planet: {planet_name} was explored. {astronauts_which_got} astronauts participated in collecting items."


        self.__unsuccesfull_misions+=1
        return "Mission is not completed."


    def report(self):
        result=f"{self.__succesfull_misions} successful missions!\n"\
               f"{self.__unsuccesfull_misions} missions were not completed!\n"\
               f"Astronauts' info:\n"
        for each_ast in self.astronaut_repository.astronauts:
            result+=f"Name: {each_ast.name}\n" \
                    f"Oxygen: {each_ast.oxygen}\n"
            if each_ast.backpack:
                result+=f"Backpack items: {', '.join(each_ast.backpack)}\n"
            else:
                result+=f"Backpack items: {'none'}\n"


        return result.strip("\n")












