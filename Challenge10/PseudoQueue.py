from .Stack import Stack
# CC11 PseudoQueue:


class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, value):
        
        '''
        This function adds an value to an exisiting stack using FIFO approuch. 
        '''

        while self.first_stack.top is not None:
            self.second_stack.push(self.first_stack.pop())
        self.first_stack.push(value)
        while self.second_stack.top is not None:
            self.first_stack.push(self.second_stack.pop())

    def dequeue(self):
        
        '''
        This function pops the last value in the stack using the FIFO approuch.
        '''
        
        if self.first_stack.is_empty():
            raise Exception("Cannot dequeue from an empty queue")

        return self.first_stack.pop().value