class Calulator:
    def __init__(self,a,b):
        self.a = a
        self.b =b
    def add(self):
        print(f"Addition : {self.a + self.b}")

    def sub(self):
        print(f"Substraction : {self.a - self.b}")
    def mul(self):
        print(f"Multi[pication : {self.a * self.b}")
    def div(self):
        print(f"Division : {self.a / self.b}")
cal = Calulator(2,3)
cal.add()
cal.sub()
cal.mul()
cal.div()
