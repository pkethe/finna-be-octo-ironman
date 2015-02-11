__author__ = 'Pranav'

class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def setNodeValue(self, value, next):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        temp = Node()
        if self.front == None:
            temp.setNodeValue(value, None)
            self.front = temp
            self.rear = temp
        else:
            temp.setNodeValue(value, None)
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):
        tempItem = self.front
        if self.front == None:
            print "No items to dequeue"
        else:
            tempItem = None
            self.front = self.front.next

        return tempItem

    def display(self):
        tempItem = self.front
        while tempItem != None:
            print str(tempItem.value) + " ",
            tempItem = tempItem.next


myQueue = Queue()

while True:
    userInput = int(raw_input("1. Queue 2. Dequeue 3. Display :"))
    if userInput == 1:
        value = int(raw_input("Enter number: "))
        myQueue.enqueue(value)
    elif userInput == 2:
        myQueue.dequeue()
    else:
        myQueue.display()



