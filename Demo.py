class Calulator:
    #a = [int(x) for x in input("Enter Numbers : ").split()]

    def __init__(self):
        self.a = []
    def accpet(self):
        list = input("Enter a list of numbers separated by spaces: ").split()
        self.a = [float(x) for x in list]
    def Add(self):

        print(f"Addition : {sum(self.a)}")
    def Sub(self):
        result = self.a[0]
        for i in self.a[1:]:
            result-=i
        print(f"Substraction : {result}")
    def Mult(self):
        result = 1
        for i in self.a:
            result *= i
        print(f"Multipication : {result}")
    def Exp(self):
        result = 1
        for i in self.a:
            result**= i
        print(f"Exponestional : {result}")
    def Div(self):
        result = self.a[0]
        for i in self.a[1:]:
            if i ==0:
                print("Divide is not possible by 0 ....")
            else :
                result/= i
        print(f"Division : {result}")

c = Calulator()

c.accpet()
print("Enter any Option ....")
print(f"1.Addition\n2.Substaraction\n3.Multipcation\n"
      f"4.Division\n5.Exponestional")
a = int(input())
if a == 1 :
    c.Add()
elif a == 2:
    c.Sub()
elif a == 3:
    c.Mult()
elif a == 4:
    c.Div()
elif a == 5:
    c.Exp()
else :
    print("Invalid input .....Try Again..")
while True:
    user_input = input("Enter 'quit' to exit or press yes to continue: ")
    if user_input.lower() == 'quit':
         break
