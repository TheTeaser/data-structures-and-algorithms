from .Queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Binary_Tree:
    def __init__(self):
        self.root = None
            
    def pre_order(self, root=None, returned_list=None):


        """
        Perform pre-order traversal on the Binary Tree and return a list of values.
        """


        if returned_list is None:
            returned_list = []
        if root is not None:
            returned_list.append(root.value)
            self.pre_order(root.left, returned_list)
            self.pre_order(root.right, returned_list)
        return returned_list

    def in_order(self, root=None, returned_list=None):
        '''
        Perform in-order traversal on the Binary Tree and return a list of values.
        '''
        if returned_list is None:
            returned_list = []
        if root is not None:
            self.in_order(root.left, returned_list)
            returned_list.append(root.value)
            self.in_order(root.right, returned_list)
        return returned_list

    def post_order(self, root=None, returned_list=None):
        '''
        Perform post-order traversal on the Binary Tree and return a list of values.
        '''
        if returned_list is None:
            returned_list = []
        if root is not None:
            self.post_order(root.left, returned_list)
            self.post_order(root.right, returned_list)
            returned_list.append(root.value)
        return returned_list
    
    def find_maximum_value(self):

        '''
        Find the maximum value stored in the Binary Tree.
        '''

        if self.root is None:
            raise ValueError("The tree is empty.")
        return self.recursive_maximum_value(self.root)

    def recursive_maximum_value(self, node):

        '''
        Recursively find the maximum value starting from the given node, Note this is a helper method for find_maximum_value().
        '''
        
        if node.right is not None:
            return self.recursive_maximum_value(node.right)
        return node.value
    
class Binary_Search_Tree(Binary_Tree):
    def __init__(self):
        super().__init__()

    def Add(self, value):
        
        '''
        Add a new node with the given value to the Binary Search Tree.
        '''

        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if self.root is None:
            self.root = Node(value)
        else:
            self.recursion(self.root, value)
     
    def recursion(self, node, value):

        '''
        Recursively traverse the Binary Search Tree to find the appropriate position for the new node.
        '''
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
                print(node.right.value)
            else:
                self.recursion(node.right, value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recursion(node.left, value)
        else:
            raise ValueError("Node with the same value already exists in the tree.")

    def Contains(self, value):

        '''
        Check if a node with the given value exists in the Binary Search Tree.
        '''
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        return self.recursive_search(self.root, value)

    def recursive_search(self, node, value):
        
        '''
        Recursively search for a node with the given value starting from the given node.
        '''
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_search(node.left, value)
        else:
            return self.recursive_search(node.right, value)

def breadth_first(tree):
    """
    Perform a breadth-first traversal of the binary tree and return a list of values.
    """
    if tree.root is None:
        raise ValueError("The tree is empty.")

    result = []
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_Empty():
        node = queue.dequeue()
        result.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result
