class Flower :
    def __init__(self,petalName,petalNum,PetalPrice):
        self.name = petalName
        self.num = petalNum
        self.price = PetalPrice
    def SetName(self,petalName):
        self.name = petalName
    
    def SetPetal(self,PetalNum):
        self.num = PetalNum

    def SetName(self,PetalPrice):
        self.price = PetalPrice

    def getName(self):
        return self.name
    
    def getPetal(self):
        return self.num

    def getPrice(self):
        return self.price

f = Flower("SunFlower",2,100)
print(f.getName())
print(f.getPetal())
print(f.getPrice())