from project.vehicle import Vehicle
from project.motorcycle import Motorcycle
from project.car import Car
from project.family_car import FamilyCar
from project.race_motorcycle import RaceMotorcycle
from project.cross_motorcycle import CrossMotorcycle
from project.sport_car import SportCar

print("--- TEST Vehicle ----")
vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

print("---- TEST Motorcycle ----")
motor=Motorcycle(50,60)
print(motor.fuel)
motor.drive(10)
print(motor.fuel_consumption)
print(motor.fuel)

print("---- TEST  Car----")

auto=Car(50,60)
print(auto.fuel_consumption)
print(auto.fuel)
auto.drive(10)
print(auto.fuel_consumption)
print(auto.fuel)

print("---- TEST  RaceMotorcycle----")

r=RaceMotorcycle(50,60)
print(r.fuel_consumption)
print(r.fuel)
r.drive(5)
print(r.fuel_consumption)
print(r.fuel)

print("---- TEST  CrossMotorcycle----")

r=CrossMotorcycle(50,60)
print(r.fuel_consumption)
print(r.fuel)
r.drive(5)
print(r.fuel_consumption)
print(r.fuel)

print("---- TEST  SportCar----")

auto=SportCar(50,60)
print(auto.fuel_consumption)
print(auto.fuel)
auto.drive(3)
print(auto.fuel_consumption)
print(auto.fuel)
print(auto.horse_power)




