class Node:
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.
        """
        self.value = value
        self.left = None
        self.right = None


class Hashtable:
    def __init__(self):
        """
        Initializes a new instance of the Hashtable class.
        """
        self.table = {}

    def add(self, key, value):
        """
        Adds a key-value pair to the hashtable.
        """
        self.table[key] = value

    def contains(self, key):
        """
        Checks if a key exists in the hashtable.
        """
        return key in self.table


def tree_intersection(tree1, tree2):
    """
    Finds the common values between two binary trees.
    """
    hashtable = Hashtable()
    get_tree_values(tree1, hashtable)
    common_values = find_common_values(tree2, hashtable)
    return common_values


def get_tree_values(root, hashtable):
    """
    Traverses a binary tree and adds its values to the hashtable.
    """
    def traverse(node):
        if node:
            hashtable.add(node.value, True)
            traverse(node.left)
            traverse(node.right)

    traverse(root)


def find_common_values(root, hashtable):
    """
    Traverses a binary tree and finds the values that exist in the hashtable.
    
    """
    common_values = set()

    def traverse(node):
        if node:
            if hashtable.contains(node.value):
                common_values.add(node.value)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return common_values


if __name__ == '__main__':
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

    print(tree_intersection(tree1, tree2))