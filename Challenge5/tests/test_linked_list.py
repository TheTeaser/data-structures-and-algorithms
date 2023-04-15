import pytest
from LinkedList.linked_list import LinkedList


def test_linked_list():
    actual =  str(LinkedList())
    expected = "Empty Linked List."
    assert actual == expected


def test_insert():
    insert_test = LinkedList()
    insert_test.insert("A")
    actual = str(insert_test)
    expected = "A --->  Null"    
    assert actual == expected


def test_search(ll):
    actual = str(ll.includes("C"))
    expected = "True"
    assert actual == expected


def test_return_all_nodes(ll):

    actual = str(ll)
    expected = "C ---> B ---> A --->  Null"    
    assert actual == expected

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A") 
    ll.insert("B") 
    ll.insert("C") 
    return ll