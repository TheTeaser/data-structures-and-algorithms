from .Node import Node

class Queue():
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