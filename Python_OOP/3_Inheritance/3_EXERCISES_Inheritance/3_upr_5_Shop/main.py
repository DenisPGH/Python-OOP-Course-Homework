from project.food import Food
from project.drink import Drink
from project.product_repository import ProductRepository
""" WRONG OUTPUT IN THE TASK !!!!!"""

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
repo.find("apple").increase(40)
print(repo)
print(food)


# [apple, water]
# water
# apple: 10
# water: 10
