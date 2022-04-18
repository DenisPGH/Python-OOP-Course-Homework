"""Create a class called Hero. Upon initialization,
it should receive a name (string) and health (number). Create two additional methods:
•	defend(damage) - reduce the given damage from the 10_upr_3_hero's health:
o	if the health become 0 or less, set it to 0 and return "{name} was defeated"
•	heal(amount) - increase the health of the 10_upr_3_hero with the given amount
"""
class Hero():
    def __init__(self,name,health):
        self.name=str(name)
        self.health=float(health)


    def defend(self,damage):
        #self.damage=damage
        self.health-=damage
        if self.health <=0:
            self.health=0
            return f"{self.name} was defeated"



    def heal(self,amount):
        #self.amount=amount
        self.health+=amount




# 10_upr_3_hero = Hero("Peter", 100)
# print(10_upr_3_hero.defend(50))
# 10_upr_3_hero.heal(50)
# print(10_upr_3_hero.defend(99))
# print(10_upr_3_hero.defend(1))
