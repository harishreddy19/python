class Node:    # creating the Node with data
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue :    # creating the Queue 
    def __init__(self):
        self.head = None 
    # method to insert the data (insert at end)
    def enqueue(self,data):
        ne = Node(data)
        temp = self.head
        if temp is None :
            self.head = ne 
        else :
            while temp.next is not None :
                temp = temp.next
            temp.next = ne 
    # method to pop an element (delete at begin)
    def dequeue(self):
        temp = self.head
        if temp is None :
            print("Queue is Empty")
        else :
            self.head = temp.next
            temp.next = None

    # method to display the data
    def display(self):
        if self.head is None :
            print("Queue is Empty")
        else :
            temp = self.head
            while temp is not None :
                print(temp.data,'-->',end='')
                temp = temp.next
            print("None")
        print()

# creating the object for Queue 
q = Queue()
while True :
    print("*Queue Implimentation using Linked List*")
    print('1.Enqueue')
    print('2.Dequeue')
    print('3.Display')
    print('4.Exit')
    k = int(input("Enter any Option..."))
    if k == 1 :
        data = input("Enter the data :")
        q.enqueue(data)
    elif k == 2 :
        q.dequeue()
    elif k == 3:
        q.display()
    elif k >= 4:
        break