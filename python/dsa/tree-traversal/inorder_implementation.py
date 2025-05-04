#!/usr/bin/python3
# Inorder Traversal of a Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Example usage
print(">> First Tree Inorder Traversal:", end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root) # Output: 4 2 5 1 3
print()

print(">> Second Tree Inorder Traversal:", end=" ")
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(5)
root1.left.left = Node(1)
root1.left.right = Node(3)

inorder_traversal(root1) # Output: 1 2 3 4 5
print()
