class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise ValueError("The queue is empty.")
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def is_Empty(self):
        return self.front is None
