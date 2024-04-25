# -*- coding: utf-8 -*-
class Building:
    """ Здание """
    def __init__(self):
        self.numberOfFloors = 100
        self.buildingType = 'Башня'

    def __eq__(self, y):
        return self.numberOfFloors == y or self.buildingType == y


c = ["Башня", 678, "Котетдж", 100, "Баня", 87]
kl = Building()
for i in range(len(c)):
    kc = c[i]
    print("True" if kl == kc else "False")




