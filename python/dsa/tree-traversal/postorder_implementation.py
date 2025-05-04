#!/usr/bin/python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")
# Example usage
print(">> First Tree Postorder Traversal:", end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder_traversal(root) # Output: 4 5 2 3 1
print()

print(">> Second Tree Postorder Traversal:", end=" ")
root1 = Node(5)
root1.left = Node(3)
root1.right = Node(4)
root1.left.left = Node(1)
root1.left.right = Node(2)

postorder_traversal(root1) # Output: 1 2 3 4 5
print()
