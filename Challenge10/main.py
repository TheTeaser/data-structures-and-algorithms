from Stack import Stack
from Queue import Queue
from Queue import PseudoQueue


stack1 = Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)

print(stack1.pop())



print("size",stack1.get_size())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print("size",stack1.get_size())

# queue1 = Queue()

# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)

# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# queue = PseudoQueue()
# queue.enqueue(5)
# print(queue)