"""Now use the classes that you have created to instantiate some animals and feed them.
 Add method feed(food) where the food will be an instance of some food classes.
Animals will only eat a specific type of food, as follows:
•	Hens eat everything
•	Mice eat vegetables and fruits
•	Cats eat vegetables and meat
•	Tigers, Dogs, and Owls eat only meat
If you try to give an animal a different type of food, it will not eat it, and you should return:
•	"{AnimalType} does not eat {FoodType}!"
The weight of an animal will increase with every piece of food it eats, as follows:
•	Hen - 0.35
•	Owl - 0.25
•	Mouse - 0.10
•	Cat - 0.30
•	Dog - 0.40
•	Tiger - 1.00
"""
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)

print("__ TEST @ __")

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

