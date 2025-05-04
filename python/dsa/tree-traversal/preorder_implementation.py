#!/usr/bin/python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Example usage
print(">> First Tree Preorder Traversal:", end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder_traversal(root) # Output: 1 2 4 5 3
print()

print(">> Second Tree Preorder Traversal:", end=" ")
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(5)
root1.left.left = Node(1)
root1.left.right = Node(3)
preorder_traversal(root1) # Output: 4 2 1 3 5
print()
