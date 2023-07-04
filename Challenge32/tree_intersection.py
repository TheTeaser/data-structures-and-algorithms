class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    values1 = get_tree_values(tree1)
    values2 = get_tree_values(tree2)
    common_values = find_common_values(values1, values2)
    return common_values


def get_tree_values(root):
    values = set()

    def traverse(node):
        if node:
            values.add(node.value)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return values


def find_common_values(set1, set2):
    common_values = set()
    for value in set1:
        if value in set2:
            common_values.add(value)
    return common_values
