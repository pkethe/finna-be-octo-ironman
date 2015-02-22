__author__ = 'Pranav'

from GenericNode import *
import sys

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Add elements into the queue
    def enqueue(self, value):
        temp = GenericNode()
        temp.value = value
        temp.next = None
        if self.front == None:
            self.front = temp
            self.rear = self.front
        else:
            if self.front == self.rear:
                self.front.next = temp
                self.rear = self.front.next
            else:
                currentRear = self.rear
                self.rear = temp
                currentRear.next = self.rear

    # Remove elements from the queue
    def dequeue(self):
        if self.front == None:
            return None
        else:
            if self.front == self.rear:
                current = self.front
                self.front = None
                self.rear = None
                return current
            else:
                current = self.front
                self.front = self.front.next
                current.next = None
                return current


    def printItemsInQueue(self):
        current = self.front
        while current != None:
            print str(current.value) + "\t"
            current = current.next


myQueue = Queue()

while True:
    userInput = int(raw_input("1. Queue 2. Dequeue 3. Display 4. Exit :"))
    if userInput == 1:
        value = int(raw_input("Enter number: "))
        myQueue.enqueue(value)
    elif userInput == 2:
        item = myQueue.dequeue()
        if item != None:
            print "Dequeued " + str(item.value)
    elif userInput == 3:
        myQueue.printItemsInQueue()
    elif userInput == 4:
        sys.exit()
    else:
        print "Invalid option, to mainloop"



