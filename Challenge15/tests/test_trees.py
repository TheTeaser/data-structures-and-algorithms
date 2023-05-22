import pytest
from Challenge15.trees import Binary_Search_Tree , Binary_Tree, Node

def test_instantiate_empty_tree():
    tree= Binary_Tree()
    actual = tree.pre_order()
    expected = []
    assert actual==expected

def test_add_child():
    tree= Binary_Search_Tree()
    tree.Add(5)
    tree.Add(4)
    tree.Add(7)
    actual = tree.in_order(tree.root)
    expected = [4,5,7]
    assert actual==expected   

def test_pre_pre_order(BST):
    assert BST.pre_order(BST.root) == [5,3,2,4,7,6,8]


def test_in_order(BST):
    assert BST.in_order(BST.root) == [2,3,4,5,6,7,8]

def test_post_order(BST):
    assert BST.post_order(BST.root) == [2,4,3,6,8,7,5]    


def test_true(BST):
    assert BST.Contains(8) == True

def test_false(BST):
    assert BST.Contains(9) == False

def test_find_maximum_value(BST):
    assert BST.find_maximum_value() == 8    

@pytest.fixture
def BST():
    BST= Binary_Search_Tree()
    BST.Add(5)
    BST.Add(3)
    BST.Add(2)
    BST.Add(4)
    BST.Add(7)
    BST.Add(6)
    BST.Add(8)
    return BST