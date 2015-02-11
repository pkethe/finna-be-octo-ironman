__author__ = 'Pranav'

class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def setNodeValue(self, value, next):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top != None:
            topItem = self.top.value
            self.top = self.top.next
            return topItem

    def push(self, value):

        if self.top == None:
            self.top = Node()
            self.top.setNodeValue(value,None)
        else:
            temp = Node()
            temp.setNodeValue(value,self.top)
            self.top = temp

    def display(self):
        if self.top == None:
            print "No Nodes"
        else:
            temp = self.top
            while temp != None:
                print temp.value
                temp = temp.next


"""
    ###Main###

"""
print "Hello"

myStack = Stack()

while True:
    userInput = int(raw_input("1. Push 2. Pop 3. Display :"))
    if userInput == 1:
        value = int(raw_input("Enter number: "))
        myStack.push(value)
    elif userInput == 2:
        myStack.pop()
    else:
        myStack.display()