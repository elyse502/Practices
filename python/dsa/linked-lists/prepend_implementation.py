#!/usr/bin/python3

class Node:
    """Node class for linked list implementation."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Append a new node to the linked list."""
        new_node = Node(value)
        # If the linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """Add a new node to the beginning of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        # If the linked list is empty
        if not self.tail:
            self.tail = new_node

    def remove(self, value):
        pass

    def iterate(self):
        pass

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")    
            current = current.next
        print("None")


# Test the linked list implementation
linked_list = LinkedList()

# When the linked list is empty, the prepend method will add a new node to the beginning of the linked list.
linked_list.prepend(0)

print(f"The head node value is: {linked_list.head.value}")
print(f"The tail node value is: {linked_list.tail.value}")
# print(f"The next node value is: {linked_list.head.next.value}")
linked_list.display()

print()
# When the linked list is not empty, the prepend method will add a new node to the beginning of the linked list.
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.prepend(-1)

print(f"The head node value is: {linked_list.head.value}")
print(f"The tail node value is: {linked_list.tail.value}")
print(f"The next node value is: {linked_list.head.next.value}")
linked_list.display()
