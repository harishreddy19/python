class Node :     # creating a node with data
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack :   # creating the Stack class 
    def __init__(self):
        self.next = None
        self.head = None
    # method to push the data into the Stack(insert at begin)
    def push_ele(self,data):
        temp = self.head
        nb = Node(data)
        if self.head is None :
            self.head = nb
        else :
            nb.next = temp
            self.head = nb
    # method to pop the element (delete at begin)
    def pop_ele(self):
        if self.head is None :
            print("Stack is Empty.")
        else :
            temp = self.head
            self.head = temp.next
            #temp.next = None
    # method to display the data 
    def display(self):
        if self.head is None :
            print("Stack is Empty")
        else :
            temp =self.head 
            while temp is not None :
                print(temp.data,'-->',end='')
                temp = temp.next
            print("None")
        print()
# creating an obj for Stack class
stk = Stack()
while True :
    print('1.Push')
    print('2.pop')
    print('3.display')
    print('4.Exit')
    k = int(input("Enter any option ...."))
    if k == 1:
        data = input("Enter the data to push ")
        stk.push_ele(data)
    elif k == 2:
        stk.pop_ele()
    elif k == 3:
        stk.display()
    elif k >= 4 :
        break