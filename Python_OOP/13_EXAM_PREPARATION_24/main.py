from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.planet.planet import Planet
from project.space_station import SpaceStation
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut import Astronaut



cosmos=SpaceStation()
planeta=Planet("MARS")
deni=Geodesist("deni")
keti=Biologist("keti")
ket=Biologist("ket")
kei=Biologist("kei")
print(cosmos.add_astronaut("Geodesist", "Keti"))
print(cosmos.add_astronaut("Biologist", "Deni"))
print(cosmos.add_astronaut("Meteorologist", "Marto"))
cosmos.add_planet("Mars","1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20")
cosmos.add_planet("Venera","1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22")
print(cosmos.send_on_mission("Mars"))
#cosmos.send_on_mission("Venera")
#cosmos.send_on_mission("Vebera")

print(cosmos.report())

# pr=PlanetRepository()
# mars=Planet("Mars")
# pr.add(mars)
# #print(pr.planets)
#
# dd=Astronaut("deni",40)
# dd.name="dddddd"