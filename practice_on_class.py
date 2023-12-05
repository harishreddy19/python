'''class Vechicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def Display(self):
        print(f"Max Speed: {self.max_speed} m/s")
        print(f"Mileage: {self.mileage} miles")
v = Vechicle(300,36)
v.Display()'
class Vechicle :
    pass

class Vehicle:2

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
v = Bus("toyota",300,37)
print(v.name)
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    pass
b = Bus("toyota",300,37)
print(b.seating_capacity())'''
