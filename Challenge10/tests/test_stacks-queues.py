
import pytest 
from Challenge10.Stack import Stack
from Challenge10.Queue import Queue
from Challenge10.Node import Node


### Stack Testing:

def test_push():
    stack = Stack()
    stack.push('A')
    excepted = stack.top.value
    assert excepted == 'A'

def test_pop():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    actual = stack.pop()
    expected = 2
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    expected = 20
    actual = stack.peek()
    assert actual == expected

def test_empty_stack():
    stack = Stack()
    expected = "This is an empty stack!"
    assert expected == stack.peek()


### Queue Testing:

def test_enqueue():
    queue = Queue()
    queue.enqueue('X')
    actual = queue.front.value
    expected = 'X'
    assert expected == actual

def test_dequeue():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(100)
    queue.dequeue()
    actual = queue.front.value
    expected = 100
    assert expected == actual

def test_peek():
    queue = Queue()
    queue.enqueue(11)
    queue.enqueue(22)
    expected = 11
    actual = queue.peek()
    assert actual == expected

def test_empty_queue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(8)
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected


