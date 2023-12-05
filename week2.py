from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def Perimeter(self):
        pass
class Triangle(Polygon):
    def __init__(self,length,bredth,height):
        self.length = length
        self.bredth = bredth
        self.height = height
    def Area(self):
        print(f"Area of the Tiangle : {0.5 * self.length * self.bredth}")
    def Perimeter(self):
        print(f"Perimiter of the Triangle : {self.length + self.bredth + self.height}")
class Quadrilateral(Polygon):
    def __init__(self,side1,side2,side3,side4):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        self.s4 = side4
    def Area(self):
        print(f"Area of The Quadrilateral is : {self.s1 * self.s2}")
    def Perimeter(self):
        print(f"Perimetrer of the Quadrilateral : {self.s1 + self.s2 + self.s3 + self.s4}")
class Pentagon(Polygon):
    def __init__(self,side):
        self.side = side
    def Area(self):
        print(f"Area of the Pentagon : {1.7204 * self.side ** 2}")
    def Perimeter(self):
        print(f"Perimeter of the Pentagon : {5 * self.side}")
tri = Triangle(3,5,6)
Qua  = Quadrilateral(3,13,21,23)
pen = Pentagon(7)
for shape in (tri , Qua , pen):
    shape.Area()
    shape.Perimeter()