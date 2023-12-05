class Car:
    def __init__(self,name,model):
        self.name = name 
        self.model = model 
    def Display(self):
        print(f"Name : {self.name}\nModelName :{self.model}")
c = Car("Toyota",2000)
c1 = Car("Maruthi",2016)
c.Display()
c1.Display()