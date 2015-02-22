__author__ = 'Pranav'

from GenericNode import *
import sys

class Stack:

    def __init__(self):
        self.top = None

    # Remove elements from the stack
    def pop(self):
        if self.top != None:
            current = self.top
            self.top = self.top.next
            current.next = None
            return current
        return None

    # Add elements into the Stack
    def push(self, value):
        temp = GenericNode()
        temp.value = value
        temp.next = None
        if self.top == None:
            self.top = temp
        else:
            temp.next = self.top
            self.top = temp

    # print elements into the stack
    def printStackElements(self):
        current = self.top
        while current != None:
            print current.value
            current = current.next

"""
    ###Main###

"""
if __name__ == '__main__':

    myStack = Stack()

    while True:
        userInput = raw_input("1. Push 2. Pop 3. Display 4. Exit: ")

        if userInput.isdigit():
            userInput = int(userInput)
            if userInput == 1:
                value = int(raw_input("Enter number: "))
                myStack.push(value)
            elif userInput == 2:
                node = myStack.pop()
                if node != None:
                    print str(node.value) + " popped"
            elif userInput == 3:
                myStack.printStackElements()
            elif userInput == 4:
                sys.exit()
            else:
                print "Invalid choice, to main loop"

            def display(self):
                if self.top == None:
                    print "No Nodes"
                else:
                    temp = self.top
                    while temp != None:
                        print temp.value
                        temp = temp.next

        else:
            print "Invalid choice, to main loop"

