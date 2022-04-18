"""The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization.
The Player also has 2 instance attributes: skills (empty dictionary that will contain the skills
of each player and its mana cost) and a guild set to "Unaffiliated" by default."""

class Player():
    def __init__(self,name,hp,mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills={}
        self.guild="Unaffiliated"

    #-	add_skill(skill_name, mana_cost)
#o	Adds the skill and the corresponding mana cost to the dictionary of skills.
    # Returns "Skill {skill_name} added to the collection of the player {player_name}"
#o	If the skill is already in the collection, returns "Skill already added"
    def add_skill(self,skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name]=mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    #-	player_info()
# o	Returns the player's information, including their skills, in this format:
# "Name: {player_name}
#  Guild: {guild_name}
#  HP: {hp}
#  MP: {mp}
#  ==={skill_name_1} - {skill_mana_cost}
#  ==={skill_name_2} - {skill_mana_cost}
#  …
#  ==={skill_name_N} - {skill_mana_cost}"
    def player_info(self):
        result=f"Name: {self.name}\n"
        result+=f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"
        for k,v in self.skills.items():
            result+= f"==={k} - {v}\n"

        return result




