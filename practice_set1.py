'''class Car :
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def Display(self):
        print(f"NAme : {self.name} \nModel : {self.model}")
c = Car("toyotta",2019)
c2 = Car("Renge Rover",2020)
c.Display()
c2.Display()

class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
    class Engine:
        def Specifications(self):
            inmodel = 2019
            hrpower = '200km/hr'
            mileage = 22
c = Car("RR",2022)'''

class Flower:
    def __init__(self,name,petals,price):
        self.name = name
        self.petals = petals
        self.price = price
    def Display(self):
        print(f"Name : {self.name}\nNO.of petals : {self.petals}\nPrice : {self.price}")
f =Flower("Jasmine",14,200)
f.Display()