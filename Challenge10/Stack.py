from .Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("This is an empty stack!")
        popped = self.top
        self.top = popped.next
        popped.next = None
        return popped.value

    def peek(self):
        if not self.top:
            return None
        return self.top.value

    def __str__(self):
        current = self.top
        output = ''
        while current:
            output += f'[{str(current.value)}]->'
            current = current.next
        return output[:-2]