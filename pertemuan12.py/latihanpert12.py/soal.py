class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

tree = BinaryTree()

tree.insert_root("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")

tree.insert_left(tree.root.left, "F")

tree.insert_left(tree.root.right, "D")
tree.insert_right(tree.root.right, "H")

tree.insert_left(tree.root.right.left, "E")
tree.insert_right(tree.root.right.left, "G")

tree.insert_left(tree.root.right.right, "I")

def inorder(node):
    if node is not None:
        print(node.data, end=" ")
        inorder(node.left)
        inorder(node.right)

inorder(tree.root)