from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self,length,bredth,height):
        self.length = length
        self.bredth = bredth
        self.height = height

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class Rectangle(Shape):
    def __init__(self,length,bredth):
        self.length = length
        self.bredth  = bredth

    def area(self):
        print(f"Area of the Rectangle : {self.length + self.bredth}")

    def Perimeter(self):
        print(f"Perimeter of Rectangle : {2 *(self.length)*(self.bredth)}")

tri = Triangle(3,43,2)
rec = Rectangle(4,5)
print(Triangle.mro())
for c in (tri,rec):
    c.area()
    c.Perimeter()