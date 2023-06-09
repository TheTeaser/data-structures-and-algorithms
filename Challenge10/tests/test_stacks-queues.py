
import pytest 
from Challenge10.Stack import Stack
from Challenge10.Queue import Queue
from Challenge10.Node import Node
from Challenge10.PseudoQueue import PseudoQueue
from Challenge10.animal_shelter import AnimalShelter

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
    expected = None
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

### PseudoQueue Testing:

def test_enqueue():
    pq = PseudoQueue()
    pq.enqueue(10)
    pq.enqueue(15)
    pq.enqueue(20)
    actual= str(pq.first_stack) 
    expected = "[10]->[15]->[20]"
    assert actual == expected



def test_dequeue():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(100)
    actual = queue.dequeue()
    expected = 7
    assert expected == actual

### Animal Shelter testing:

def test_enqueue_dequeue():
    shelter = AnimalShelter()

    shelter.enqueue({"species": "cat", "name": "Luna"})
    shelter.enqueue({"species": "dog", "name": "Buddy"})
    
    animal1 = {
        "species" : "cat",
        "name": "Whiskers"
    }

    animal2 = {
        "species" : "dog",
        "name": "Rocky"
    }

    shelter.enqueue(animal1)
    shelter.enqueue(animal2)

    actual1 = shelter.dequeue("cat")
    expected1 = {"species": "cat", "name": "Luna"}
    assert actual1 == expected1

    actual2 = shelter.dequeue("dog")
    expected2 = {"species": "dog", "name": "Buddy"}
    assert actual2 == expected2

