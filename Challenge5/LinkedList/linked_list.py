class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,value):
        node = Node(value)
        node.next =self.head
        self.head = node

    def includes(self,key):
        temp = self.head
        while(temp):
            if temp.value == key:
                return True
            else:
               temp = temp.next
        return False

    
    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty Linked List."
        else:
            current = self.head
            while(current):
                output += f'{current.value} ---> '
                current = current.next
            
            output += " Null"
        return output

