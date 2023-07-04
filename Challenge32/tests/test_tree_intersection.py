from Challenge32.tree_intersection import Node, tree_intersection
import pytest

def test_tree_intersection_with_common_values():
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)
    tree1.left.right = Node(5)
    tree1.right.left = Node(6)
    tree1.right.right = Node(7)

    tree2 = Node(2)
    tree2.left = Node(4)
    tree2.right = Node(6)
    tree2.left.left = Node(8)
    tree2.left.right = Node(9)
    tree2.right.left = Node(10)
    tree2.right.right = Node(11)

    assert tree_intersection(tree1, tree2) == {2, 4, 6}


def test_tree_intersection_with_no_common_values():
    tree3 = Node(1)
    tree3.left = Node(2)
    tree3.right = Node(3)
    tree3.left.left = Node(4)
    tree3.left.right = Node(5)
    tree3.right.left = Node(6)
    tree3.right.right = Node(7)

    tree4 = Node(8)
    tree4.left = Node(9)
    tree4.right = Node(10)

    assert tree_intersection(tree3, tree4) == set()


def test_tree_intersection_with_partial_overlap():
    tree5 = Node(1)
    tree5.left = Node(2)
    tree5.right = Node(3)
    tree5.left.left = Node(4)
    tree5.left.right = Node(5)

    tree6 = Node(1)
    tree6.left = Node(2)
    tree6.right = Node(3)
    tree6.left.left = Node(5)

    assert tree_intersection(tree5, tree6) == {1, 2, 3, 5}