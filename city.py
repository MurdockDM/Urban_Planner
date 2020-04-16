class City:
    def __init__(self, name, mayor, yearEstablished):
        self.city_name = name
        self.mayor = mayor
        self.year = yearEstablished
        self.buildings = list()


    def add_building(self, building_name):
        self.buildings.append(building_name)  

    