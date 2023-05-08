from .Node import Node
from .Stack import Stack

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            self.front.value
        except:
            return "This is an empty queue!"
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    def peek(self):
        try:
            return self.front.value
        except:
            return "This is an empty queue!"

    def is_Empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False
    
    

# CC11 PseudoQueue:


class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, value):
        while self.first_stack.top is not None:
            self.second_stack.push(self.first_stack.pop())
        self.first_stack.push(value)
        while self.second_stack.top is not None:
            self.first_stack.push(self.second_stack.pop())

    def dequeue(self):
        if self.first_stack.is_empty():
            raise Exception("Cannot dequeue from an empty queue")

        return self.first_stack.pop().value