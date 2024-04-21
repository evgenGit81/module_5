# -*- coding: utf-8 -*-
class House:
    def __init__(self):
        self.name = "Big house"
    def abouthouse(self):
        print("Пентхаус Трампа с девченками.")


house = House()
house.numberOfFloor = 0
while house.numberOfFloor < 70:
    house.numberOfFloor += 1
    print(f"Текущий этаж равен {house.numberOfFloor}")
    if house.numberOfFloor == 70:
        house.abouthouse()
