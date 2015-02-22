__author__ = 'Pranav'


from GenericNode import *
import sys

class SingleLinkedList:

    def __init__(self):
        self.root = None
    
    # Insert new node
    def insert(self, value):
        # Create new node
        temp = GenericNode()
        temp.value = value
        temp.next = None
        if self.root == None:
            self.root = temp
        else:
            current = self.root
            while current.next != None:
                current = current.next

            current.next = temp

    # Search a node
    def search(self, value):
        current = self.root

        if current == value:
            return True
        else:
            while current.next != None:
                if current.value == value:
                    return True
                else:
                    current = current.next

            return False


    # Print Linked list
    def printLinkedList(self):
        current = self.root

        # Iterate over list
        while current != None:
            print str(current.value) + "\t"
            current = current.next


    # Delete item in the Linked list
    def deleteItemInLinkedList(self, value):
        if self.root.value == value:
            temp = self.root
            self.root = self.root.next
            temp = None
        else:
            current = self.root.next
            previous = self.root
            while current != None:

                if current.value == value:
                    if current.next == None:
                        previous.next = None
                    else:
                        previous.next = current.next

                    current = None
                else:
                    previous = current
                    current = current.next


''' Main start '''
if __name__=='__main__':
    sll = SingleLinkedList()

    while True:
        userChoice = raw_input('1. Insert, 2. Delete, 3. Print, 4. Exit : ')

        if userChoice.isdigit():
            userChoice = int(userChoice)
            if (userChoice == 1 or userChoice == 2):
                input = raw_input("Enter the number:")
                if input.isdigit():

                    if userChoice ==1:
                        sll.insert(int(input))
                    elif userChoice ==2:
                        sll.deleteItemInLinkedList(int(input))
                    else:
                        print "Invalid input"
                else:
                    print "Invalid input format"
            elif userChoice == 3:
                sll.printLinkedList()
            elif userChoice == 4:
                sys.exit()
            else:
                print "Invalid choice"
        else:
            print "Enter valid input"

