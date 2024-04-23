# -*- coding: utf-8 -*-
class House:
    def __init__(self):
        self.numberOfFloors = 10
    def abouthouse(self):
        print("Пентхаус Трампа с девченками.")


house = House()
numFloor = 0
for i in range(house.numberOfFloors):
    numFloor = i + 1
    print(f"Текущий этаж равен {numFloor}")
    if numFloor == 10:
       house.abouthouse())
