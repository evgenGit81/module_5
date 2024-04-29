# -*- coding: utf-8 -*-
class Building:
    """ Здание """

    def __init__(self, numberOfFloors=int, buildingType=str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


numfloors = Building(100, "Башня")
buildtype = Building(200, "Башня")
print(numfloors == buildtype)
