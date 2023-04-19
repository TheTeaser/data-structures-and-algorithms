import pytest
from LinkedList.linked_list import LinkedList


def test_linked_list():
    actual = str(LinkedList())
    expected = "Empty Linked List."
    assert actual == expected


def test_insert():
    insert_test = LinkedList()
    insert_test.insert("A")
    actual = str(insert_test)
    expected = "A ---> Null"
    assert actual == expected


def test_search(ll):
    actual = str(ll.includes("C"))
    expected = "True"
    assert actual == expected

def test_return_all_nodes(ll):
    actual = str(ll)
    expected = "D ---> C ---> B ---> A ---> Null"
    assert actual == expected

# tests for append(), insert_before(), insert_after() & delete() methods:

def test_append(ll):
    ll.append("E")
    actual = str(ll)
    expected = "D ---> C ---> B ---> A ---> E ---> Null"
    assert actual == expected


def test_insert_before(ll):
    ll.insert_before("B", "X")
    actual = str(ll)
    expected = "D ---> C ---> X ---> B ---> A ---> Null"
    assert actual == expected


def test_insert_after(ll):
    ll.insert_after("B", "Y")
    actual = str(ll)
    expected = "D ---> C ---> B ---> Y ---> A ---> Null"
    assert actual == expected


def test_delete(ll):
    ll.delete("B")
    actual = str(ll)
    expected = "D ---> C ---> A ---> Null"
    assert actual == expected

# Tests for kthFromEnd()

def test_kthFromEnd01(ll):
    expected = "A"
    actual = ll.kthFromEnd(1)
    assert actual == expected

def test_kthFromEnd02(ll):
    expected = "C"
    actual = ll.kthFromEnd(3)
    assert actual == expected


def test_kthFromEnd03(ll):
    expected = "Error! You have inserted an index bigger than or equal to the list's whole length, please try again."
    with pytest.raises(ValueError, match=expected):
        ll.kthFromEnd(6)





@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    ll.insert("C")
    ll.insert("D")
    return ll