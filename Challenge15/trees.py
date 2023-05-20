class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Binary_Tree:
    def __init__(self):
        self.root = None
            
    def pre_order(self, root=None, returned_list=None):
        if returned_list is None:
            returned_list = []
        if root is not None:
            returned_list.append(root.value)
            self.pre_order(root.left, returned_list)
            self.pre_order(root.right, returned_list)
        return returned_list

    def in_order(self, root=None, returned_list=None):
        if returned_list is None:
            returned_list = []
        if root is not None:
            self.in_order(root.left, returned_list)
            returned_list.append(root.value)
            self.in_order(root.right, returned_list)
        return returned_list

    def post_order(self, root=None, returned_list=None):
        if returned_list is None:
            returned_list = []
        if root is not None:
            self.post_order(root.left, returned_list)
            self.post_order(root.right, returned_list)
            returned_list.append(root.value)
        return returned_list
    
class Binary_Search_Tree(Binary_Tree):
    def __init__(self):
        super().__init__()

    def Add(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if self.root is None:
            self.root = Node(value)
        else:
            self.recursion(self.root, value)
     
    def recursion(self, node, value):
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
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        return self.recursive_search(self.root, value)

    def recursive_search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_search(node.left, value)
        else:
            return self.recursive_search(node.right, value)

