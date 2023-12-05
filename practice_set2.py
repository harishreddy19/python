'''class Circle:
    pi = 3.14
    def __init__(self,radius):
       self.radius = radius

    def area(self):
        print(f"The area of the Circle : {Circle.pi * self.radius * self.radius}")

    def peremeter(self):
        print(f"The premetr of the circle is : {2 * Circle.pi * self.radius}")

cle = Circle(4)
cle.area()
cle.peremeter()

'''

'''class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.dob = date_of_birth
person1 = Person('rajesh','India',65)
print(person1.dob)
print(person1.name)
print(person1.country)'''


'''class Calcutor:
    def __init__(self,num1,num2):
        self.num1 =  num1
        self.num2 = num2
    def add(self):
        print(f'Addition : {self.num1 + self.num2}')
    def sub(self):
        print(f"Substraction : {self.num1 - self.num2}")
    def div(self):
        print(f"Division : {self.num1 / self.num2}")
    def mul(self):
        print(f'Multipication : {self.num1 * self.num2}')
cla = Calcutor(22 , 45)
cla.add()
cla.sub()
cla.div()
cla.mul()'''

class Shape:
    pi = 3.14
    def area(self):
        pass
    def preimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Arae of the Circle : {Shape.pi * self.radius * self.radius}")
    def preimeter(self):
        print(f"The PrImeter of the Circle is : {2 * Shape.pi * self.radius}")
class Triangle(Shape):
    def __init__(self, length, bre, hei):
        self.len = length
        self.bre = bre
        self.hei = hei
    def area(self):
        print(f"The Area of the Triangle : {0.5 * self.len * self.bre * self.hei}")
    def preimeter(self):
        print(f"The preimetr of the Triangle : {0.5 * self.len * self.bre}")
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(f'Area of the Square : {self.side * self.side * self.side}')
    def preimeter(self):
        print(f"The preimeter of the Sqwuare : {self.side * self .side}")
cle = Circle(3)
cle.area()
cle.preimeter()
sqe = Square(5)
sqe.area()
sqe.preimeter()
trii = Triangle(5,7,8)
trii.area()
trii.preimeter()