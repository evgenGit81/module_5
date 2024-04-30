# -*- coding: utf-8 -*-
class Building:
    """ Здания """
    total = 0

    def __init__(self):
        Building.total += 1


build = 40
list_building = []
for i in range(build):
    new_building = Building()
    list_building.append(new_building.total)
print(list_building)
    