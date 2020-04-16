from building import Building
from city import City

megalopolis = City("Megalopolis", "Rob Morrisroe", 1927)

buildings = [Building("505 West Avenue", 3), Building("404 East Avenue", 14), Building("303 North Avenue", 9), Building("202 South Avenue", 18), Building("101 West Boulevard", 7)]


for building in buildings:
    building.purchase("Robert Robertson")
    building.construct()
    megalopolis.add_building(building)
    building.printOut()

    

