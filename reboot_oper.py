# -*- coding: utf-8 -*-
class Building:
    """ Здание """

    def __init__(self, numberOfFloors = 100, buildingType = "Башня"):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


builfr = {"Башня": 100, "Котетдж": 3, "Баня": 2}
numfloors = Building()
buildtype = Building()
print(numfloors == Building() and buildtype == Building())
for key in builfr.keys():
    print(numfloors == Building(numberOfFloors=builfr[key]) and buildtype == Building(buildingType=key))
    
