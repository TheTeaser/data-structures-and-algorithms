from .Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        try:
            deleted_value = self.top.value
            temp = self.top.next
            self.top = temp
            temp.next = None
            return deleted_value
        except:
            return "This is an empty stack!"

    def peek(self):
        try:
            return self.top.value
        except:
            return "This is an empty stack!"

    def is_Empty(self):
        if self.top == None:
            return False
        else:
            return True
