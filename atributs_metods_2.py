# -*- coding: utf-8 -*-
class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNumberOfFloors(self, floor):
        self.numberOfFloors = floor
        print("Номер этажа: ", self.numberOfFloors)


house = House()
floor = 0

while floor < 70:
    floor += 1
    house.setNumberOfFloors(floor)

